# isolationforest_detector.py - Baseline ML ligero para Cowrie (Giovanni Lorusso, 2025)
# Detección de anomalías + mutación automática de banners

import json
import time
import random
from datetime import datetime
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import pandas as pd
import os

# Banners para mutación (realistas 2025)
BANNERS = [
    "SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.1",
    "SSH-2.0-OpenSSH_9.3p1 Debian-3",
    "SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.7",
    "SSH-2.0-OpenSSH_9.6p1 Ubuntu-3ubuntu13"
]

# Configuración
LOG_FILE = "/cowrie/var/log/cowrie/cowrie.json"
CONFIG_FILE = "/cowrie/etc/cowrie.cfg"
MUTATION_THRESHOLD = 500  # Mutar banner cada 500 sesiones sospechosas
CONTAMINATION = 0.1       # % esperado de anomalías
TRAINING_SAMPLES = 100    # Mínimo para entrenamiento inicial

class CowrieAnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=CONTAMINATION, random_state=42)
        self.scaler = StandardScaler()
        self.session_count = 0
        self.anomaly_count = 0
        self.train_data = []
        self.last_mutation = 0

    def extract_features(self, event):
        """Extrae features de evento Cowrie"""
        try:
            duration = event.get('duration', 0)
            commands = len(event.get('commands', []))
            input_bytes = event.get('bytes_in', 0)
            output_bytes = event.get('bytes_out', 0)
            return [duration, commands, input_bytes, output_bytes]
        except:
            return [0, 0, 0, 0]

    def mutate_banner(self):
        """Mutar banner en cowrie.cfg y reload Cowrie"""
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
            # Reload Cowrie (sin reiniciar contenedor)
            os.system("pkill -HUP -f cowrie")
            print(f"[{datetime.now()}] Banner mutado a: {new_banner}")
        except Exception as e:
            print(f"Error mutando banner: {e}")

    def process_log(self):
        """Monitorear logs en tiempo real"""
        try:
            with open(LOG_FILE, 'r') as f:
                f.seek(0, os.SEEK_END)  # Ir al final
                while True:
                    line = f.readline()
                    if not line:
                        time.sleep(0.5)
                        continue
                    try:
                        event = json.loads(line.strip())
                        if event.get('eventid') == 'cowrie.session.closed':
                            features = self.extract_features(event)
                            self.session_count += 1

                            # Acumular para entrenamiento
                            self.train_data.append(features)

                            if len(self.train_data) >= TRAINING_SAMPLES:
                                df = pd.DataFrame(self.train_data)
                                scaled = self.scaler.fit_transform(df)
                                self.model.fit(scaled)
                                
                                # Predicción en sesión actual
                                pred = self.model.predict([self.scaler.transform([features])])[0]
                                if pred == -1:  # Anomalía
                                    self.anomaly_count += 1
                                    print(f"[{datetime.now()}] Anomalía detectada en sesión {self.session_count}")

                                # Mutación si threshold
                                if (self.anomaly_count > 10 or self.session_count - self.last_mutation > MUTATION_THRESHOLD):
                                    self.mutate_banner()
                                    self.last_mutation = self.session_count
                                    self.anomaly_count = 0

                    except json.JSONDecodeError:
                        continue
        except Exception as e:
            print(f"Error leyendo logs: {e}")
            time.sleep(5)

if __name__ == "__main__":
    print(f"[{datetime.now()}] Baseline Cowrie + Isolation Forest iniciado (Giovanni Lorusso, 2025)")
    detector = CowrieAnomalyDetector()
    detector.process_log()
