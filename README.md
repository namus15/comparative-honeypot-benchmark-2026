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

# Despliega todo el cluster
ansible-playbook -i inventory.ini deploy-honeypots.yml
