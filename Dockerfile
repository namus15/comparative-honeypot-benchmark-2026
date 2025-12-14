FROM cowrie/cowrie:latest

# Instalar dependencias para Isolation Forest y monitoreo
RUN pip install --no-cache-dir scikit-learn pandas prometheus-client

# Copiar configuración y script del baseline
COPY cowrie.cfg /cowrie/etc/cowrie.cfg
COPY isolationforest_detector.py /cowrie/src/isolationforest_detector.py

# Ejecutar Cowrie + detector en paralelo
CMD /opt/cowrie/bin/cowrie start -n && python /cowrie/src/isolationforest_detector.py
