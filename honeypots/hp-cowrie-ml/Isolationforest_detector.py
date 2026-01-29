# isolationforest_detector.py
# Baseline propio: detección de anomalías con Isolation Forest + mutación de banners
# Autor: Giovanni Carlos Lorusso Montiel (2026)

import json
import time
from datetime import datetime
import numpy as np
from sklearn.ensemble import IsolationForest
from cowrie.core import output

class IsolationForestDetector(output.Output):
    """
    Detector de anomalías basado en Isolation Forest.
    - Entrena con sesiones normales
    - Detecta anomalías (pred = -1)
    - Si streak de anomalías > 10 → muta banner SSH
    """

    def __init__(self):
        self.model = IsolationForest(
            contamination=0.1,          # 10% esperado de anomalías
            n_estimators=100,
            max_samples=256,
            random_state=42
        )
        self.session_features = {}      # Almacena características por sesión
        self.anomaly_streak = {}        # Contador de anomalías consecutivas
        self.banner_list = [
            "SSH-2.0-OpenSSH_9.3p1 Debian-3deb12u1",
            "SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.1",
            "SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.7",
            "SSH-2.0-OpenSSH_9.6p1 Ubuntu-3ubuntu13.3"
        ]
        self.banner_index = 0

    def start(self):
        pass

    def stop(self):
        pass

    def ocsf(self, data):
        """Evento de Cowrie en formato OCSF"""
        session = data.get("session", "unknown")
        if session not in self.session_features:
            self.session_features[session] = []
            self.anomaly_streak[session] = 0

        # Extraer características simples (ejemplo)
        feature = [
            data.get("duration", 0),
            len(data.get("input", "")),
            data.get("bytes_in", 0),
            data.get("bytes_out", 0),
            1 if "success" in data.get("eventid", "") else 0
        ]

        self.session_features[session].append(feature)

        # Si hay suficientes muestras → predecir
        if len(self.session_features[session]) >= 10:
            X = np.array(self.session_features[session][-10:])
            pred = self.model.fit_predict(X)
            last_pred = pred[-1]

            if last_pred == -1:
                self.anomaly_streak[session] += 1
                print(f"[ANOMALY DETECTED] Session {session} - Streak: {self.anomaly_streak[session]}")

                if self.anomaly_streak[session] > 10:
                    self.mutate_banner()
                    self.anomaly_streak[session] = 0  # Reset
            else:
                self.anomaly_streak[session] = 0

    def mutate_banner(self):
        """Muta el banner SSH para evadir fingerprinting"""
        self.banner_index = (self.banner_index + 1) % len(self.banner_list)
        new_banner = self.banner_list[self.banner_index]
        print(f"[BANNER MUTATED] New banner: {new_banner}")
        # Aquí va la lógica real para cambiar banner en Cowrie (via config o hook)

    # Métodos requeridos por Cowrie Output
    def write(self, data):
        self.ocsf(data)

    def log(self, *args, **kwargs):
        pass
