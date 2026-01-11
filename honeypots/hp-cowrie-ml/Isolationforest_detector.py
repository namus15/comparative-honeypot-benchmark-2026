# isolationforest_detector.py
# Baseline ML ligero para Cowrie: Detección de anomalías + mutación automática de banners
# Autor: Dr. Giovanni Carlos Lorusso Montiel (2026)
# Licencia: CC-BY-4.0

import json
import time
import random
import os
from datetime import datetime
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Configuración
LOG_FILE = "/cowrie/var/log/cowrie/cowrie.json"
CONFIG_FILE = "/cowrie/etc/cowrie.cfg"
BANNERS = [
    "SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.1",
    "SSH-2.0-OpenSSH_9.3p1 Debian-3deb12u1",
    "SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.7",
    "SSH-2.0-OpenSSH_9.6p1 Ubuntu-3ubuntu13.3"
]
MUTATION_THRESHOLD = 500  # Mutar cada 500 sesiones
ANOMALY_THRESHOLD = 10    # Mutar si >10 anomalías seguidas
CONTAMINATION = 0.1       # % esperado de anomalías
TRAINING_SAMPLES = 200    # Mínimo para entrenamiento

class CowrieMLBaseline:
    def __init__(self):
        self.model = IsolationForest(contamination=CONTAMINATION, random_state=42)
        self.scaler = StandardScaler()
        self.session_count = 0
        self.anomaly_streak = 0
        self.train_data = []
        self.last_mutation = 0
        print(f"[{datetime.now()}] Baseline Cowrie + Isolation Forest iniciado")

    def extract_features(self, event):
        """Features: duración, comandos, bytes in/out"""
        try:
            duration = event.get('duration', 0)
            commands = len(event.get('commands', []))
            bytes_in = event.get('bytes_in', 0)
            bytes_out = event.get('bytes_out', 0)
            return [duration, commands, bytes_in + bytes_out]
        except:
            return [0, 0, 0]

    def mutate_banner(self):
        """Mutar banner en config y reload Cowrie"""
        new_banner = random.choice(BANNERS)
        try:
            with open(CONFIG_FILE, 'r') as f:
                lines = f.readlines()
            with open(CONFIG_FILE, 'w') as f:
                for line in lines:
                    if line.strip().startswith('version ='):
                        f.write(f"version = {new_banner}\n")
                    else:
                        f.write(line)
            os.system("pkill -HUP -f cowrie")  # Reload sin restart
            print(f"[{datetime.now()}] Banner mutado a: {new_banner}")
            self.last_mutation = self.session_count
            self.anomaly_streak = 0
        except Exception as e:
            print(f"[{datetime.now()}] Error mutando banner: {e}")

    def run(self):
        """Loop principal: monitorear logs en tiempo real"""
        try:
            with open(LOG_FILE, 'r') as f:
                f.seek(0, os.SEEK_END)
                while True:
                    line = f.readline()
                    if not line:
                        time.sleep(0.5)
                        continue
                    try:
                        event = json.loads(line.strip())
                        if event.get('eventid') in ['cowrie.session.closed', 'cowrie.login.failed']:
                            features = self.extract_features(event)
                            self.session_count += 1

                            self.train_data.append(features)

                            if len(self.train_data) >= TRAINING_SAMPLES:
                                df = pd.DataFrame(self.train_data[-TRAINING_SAMPLES:])
                                scaled = self.scaler.fit_transform(df)
                                self.model.fit(scaled)

                                pred = self.model.predict([self.scaler.transform([features])])[0]
                                if pred == -1:  # Anomalía
                                    self.anomaly_streak += 1
                                    print(f"[{datetime.now()}] Anomalía detectada (sesión {self.session_count})")
                                else:
                                    self.anomaly_streak = max(0, self.anomaly_streak - 1)

                                # Mutación por threshold o streak
                                if (self.anomaly_streak >= ANOMALY_THRESHOLD or 
                                    self.session_count - self.last_mutation >= MUTATION_THRESHOLD):
                                    self.mutate_banner()

                    except Exception as e:
                        print(f"[{datetime.now()}] Error procesando línea: {e}")
        except Exception as e:
            print(f"[{datetime.now()}] Error crítico: {e}")
            time.sleep(10)

if __name__ == "__main__":
    detector = CowrieMLBaseline()
    detector.run()
