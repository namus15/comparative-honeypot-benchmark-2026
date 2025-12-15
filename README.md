# Comparative Honeypot Benchmark 2026 – Tesis Postdoctoral UNICEPES

**Autor:** Dr. Giovanni Carlos Lorusso Montiel  
**ORCID:** 0000-0002-3122-8142  
**Email:** al6391@unicepes.edu.mx  
**DOI Dataset:**(https://zenodo.org/badge/DOI/10.5281/zenodo.17688915.svg)](https://doi.org/10.5281/zenodo.17688915) 

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17688916.svg)](https://doi.org/10.5281/zenodo.17688916)

## Descripción
Benchmark concurrente de 60 días (noviembre 2025 – enero 2026) entre honeypots tradicionales y ML-enhanced. Incluye despliegue real en Hetzner Cloud, métricas, análisis AHP-TOPSIS y tesis postdoctoral completa.

**Estado actual (24 nov 2025 – Día 3):** 5 % completado – 2,498 eventos reales procesados. ML-enhanced superan en 68 % a tradicionales.

## Archivos Principales
- **Tesis_Postdoctoral_Giovanni_Lorusso_2026.pdf** (200 páginas) – Tesis completa con datos reales Día 3.
- `honeypots/` – Docker Compose para cada honeypot.
- `deploy-honeypots.yml` – Ansible para despliegue.
- `inventory.ini` – IPs reales del cluster.

## Honeypots Evaluados
| Honeypot | Tipo | IP Real | Tráfico Día 3 |
|----------|------|---------|---------------|
| T-Pot 24.04 | Tradicional | 95.216.163.182 | 580 |
| Cowrie | Tradicional | 78.46.221.115 | 380 |
| Artifice | ML | 116.203.34.92 | 460 |
| HoneyGAN | ML | 185.233.152.214 | 390 |
| Cowrie + Isolation Forest | Propio | 49.12.127.18 | 440 |

## Uso Rápido|

## Uso rápido
```bash
git clone https://github.com/namus15/comparative-honeypot-benchmark-2026.git
cd comparative-honeypot-benchmark-2026
ansible-playbook -i inventory.ini deploy-honeypots.yml
# Cowrie + Isolation Forest (Baseline ML-enhanced 2026)

**Aporte original**: Dr. Giovanni Carlos Lorusso Montiel

**Descripción**: Extensión ligera de Cowrie con Isolation Forest (scikit-learn) para detección de anomalías en tiempo real + mutación automática de banners SSH.

**Características**:
- Detección no supervisada de sesiones maliciosas
- Mutación de banner cada 500 sesiones o streak de anomalías
- Bajo consumo (~34% CPU promedio)
- Logs JSON para análisis fácil

**Despliegue**:
## Baseline Cowrie + Isolation Forest
Código completo: honeypots/hp-cowrie-ml/
Aporte original: Detección anomalías + mutación banners.
```bash
docker-compose up -d
