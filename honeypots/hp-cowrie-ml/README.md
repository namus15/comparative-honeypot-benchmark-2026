# Cowrie + Isolation Forest (Baseline ML-enhanced 2026)

**Aporte original**: Dr. Giovanni Carlos Lorusso Montiel

**Descripción**: Extensión ligera de Cowrie con Isolation Forest para detección de anomalías en tiempo real + mutación automática de banners SSH.

**Características**:
- Detección no supervisada de sesiones maliciosas
- Mutación de banner cada 500 sesiones o streak de anomalías
- Bajo consumo (~34% CPU promedio)
- Logs JSON para análisis fácil

**Despliegue**:
```bash
docker-compose up -d
