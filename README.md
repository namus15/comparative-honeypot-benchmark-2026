# Comparative Honeypot Benchmark 2026

**Autor:** Dr. Giovanni Carlos Lorusso Montiel  
**ORCID:** [0000-0002-3122-8142](https://orcid.org/0000-0002-3122-8142)  
**Afiliación:** Universidad Centro Panamericano de Estudios Superiores (UNICEPES), México  
**Email:** al6391@unicepes.edu.mx  

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17688916.svg)](https://doi.org/10.5281/zenodo.17688916)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Descripción
Benchmark comparativo concurrente de 60 días (enero–marzo 2026) entre honeypots tradicionales y mejorados con aprendizaje automático.  
Incluye despliegue real en 5 máquinas Hetzner Cloud, métricas de rendimiento, consumo de recursos y análisis económico.

**Dataset permanente (embargo hasta 31/03/2026):**  
https://doi.org/10.5281/zenodo.17688916

**Artículo publicado (próximamente):** Revista Telematique

## Estructura del repositorio
- `honeypots/` → Docker Compose de cada honeypot
- `deploy-honeypots.yml` → Ansible para despliegue automático
- `inventory.ini` → IPs reales del cluster
- `analysis-notebooks/` → Jupyter con todo el análisis estadístico

## Honeypots evaluados
| Honeypot                  | Tipo                     | IP Real             | Repositorio |
|---------------------------|--------------------------|---------------------|-----------|
| T-Pot 24.04               | Tradicional              | 95.216.163.182     | oficial |
| Cowrie                    | Tradicional              | 78.46.221.115       | oficial |
| Artifice                  | ML-enhanced (RNN)        | 116.203.34.92       | oficial |
| HoneyGAN                  | ML-enhanced (GAN)        | 185.233.152.214     | oficial |
| Cowrie + Isolation Forest | Contribución original    | 49.12.127.18        | este repo |

## Uso rápido
```bash
git clone https://github.com/namus15/comparative-honeypot-benchmark-2026.git
cd comparative-honeypot-benchmark-2026
ansible-playbook -i inventory.ini deploy-honeypots.yml
