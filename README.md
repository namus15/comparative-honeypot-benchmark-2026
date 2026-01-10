# Comparative Honeypot Benchmark 2026

**Artículo científico**  
Análisis comparativo del rendimiento, consumo de recursos y costos operacionales de honeypots modernos: tradicionales frente a mejorados con aprendizaje automático (2022–2026)

**Autor**: Dr. Giovanni Carlos Lorusso Montiel  
**ORCID**: 0000-0002-3122-8142  
**Afiliación**: Universidad Centro Panamericano de Estudios Superiores (UNICEPES), México / Universidad de Toronto, Canadá

## Resumen
Evaluación concurrente de 6 honeypots open-source (3 tradicionales, 3 ML-enhanced) en tráfico real replicado (Hetzner Cloud, Alemania). Métricas: detección/interacción, evasión fingerprinting, recursos y TCO/ROI.

Dataset público (embargo hasta 31/03/2026):  
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17688915.svg)](https://doi.org/10.5281/zenodo.17688915)

## Infraestructura (Hetzner Cloud)
| Honeypot                          | IP Pública           |
|-----------------------------------|----------------------|
| T-Pot 24.04                       | 95.216.163.182       |
| Cowrie 2024.2                     | 78.46.221.115        |
| Dionaea 2024.1                    | (en despliegue)      |
| Artifice (ML-enhanced)            | 116.203.34.92        |
| HoneyGAN (ML-enhanced)            | 185.233.152.214      |
| Cowrie + Isolation Forest (baseline) | 49.12.127.18      |
| Monitor central                   | 159.69.63.241        |

## Despliegue
```bash
# Copia plantilla
cp inventory.example.ini inventory.ini

# Edita inventory.ini con tus IPs
## Estructura honeypots
- hp-tpot: T-Pot 24.04
- hp-cowrie: Cowrie puro
- hp-dionaea: Dionaea
- hp-artifice: Artifice (RNN SSH)
- hp-honeygan: HoneyGAN equivalente
- hp-cowrie-ml: Baseline Cowrie + Isolation Forest (aporte original)
- hp-artifice: Artifice (RNN SSH)
- hp-honeygan: HoneyGAN equivalente
- hp-cowrie-ml: Baseline Cowrie + Isolation Forest (aporte original)

# Despliega todo el cluster
ansible-playbook -i inventory.ini deploy-honeypots.yml
# Comparative Honeypot Benchmark 2026

**Título del artículo**: Análisis comparativo del rendimiento, consumo de recursos y costos operacionales de honeypots modernos: tradicionales frente a mejorados con aprendizaje automático (2022–2026)

**Autor**: Dr. Giovanni Carlos Lorusso Montiel  
**ORCID**: 0000-0002-3122-8142  
**Afiliación**: Universidad Centro Panamericano de Estudios Superiores (UNICEPES), México / Universidad de Toronto, Canadá  
**Emails**: al6391@unicepes.edu.mx | namus15@gmail.com

## Resumen
Primera evaluación comparativa concurrente de 6 honeypots open-source (3 tradicionales: T-Pot 24.04, Cowrie 2024.2, Dionaea 2024.1; 3 ML-enhanced: Artifice, HoneyGAN, baseline propio Cowrie + Isolation Forest). Desplegados simultáneamente 60 días (enero-marzo 2026) en Hetzner Cloud (Alemania) con tráfico real replicado (tcpreplay). Resultados: ML-enhanced +63-105% interacción útil, evasión fingerprinting +42-67%, ROI 8-11 meses.

**Dataset público (embargo hasta 31/03/2026)**:  
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17688915.svg)](https://doi.org/10.5281/zenodo.17688915)

## Infraestructura Real (Hetzner Cloud – Alemania)
| Honeypot                          | IP Pública           | Tipo                     |
|-----------------------------------|----------------------|--------------------------|
| Central (Monitor + tcpreplay)     | 159.69.63.241       | Monitorización           |
| T-Pot 24.04                       | 95.216.163.182      | Tradicional multi        |
| Cowrie 2024.2                     | 78.46.221.115       | Tradicional SSH/Telnet   |
| Dionaea 2024.1                    | (en despliegue)     | Tradicional malware      |
| Artifice (ML-enhanced)            | 116.203.34.92       | RNN respuestas dinámicas |
| HoneyGAN (ML-enhanced)            | 185.233.152.214     | GAN respuestas creíbles  |
| Cowrie + Isolation Forest (propio)| 49.12.127.18        | Baseline anomalías       |

## Estructura del Repositorio
- `honeypots/` → Configuraciones Docker Compose por honeypot
  - hp-tpot/
  - hp-cowrie/
  - hp-dionaea/
  - hp-artifice/
  - hp-honeygan/
  - hp-cowrie-ml/ (baseline propio: Dockerfile, cowrie.cfg, isolationforest_detector.py)
- `deploy-honeypots.yml` → Playbook Ansible completo
- `inventory.example.ini` → Plantilla para tus IPs reales
- `notebooks/` → Jupyter para análisis estadístico (limpieza, interacción, fingerprinting, recursos, costos, pruebas estadísticas)

