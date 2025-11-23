# comparative-honeypot-benchmark-2026
Benchmark comparativo de honeypots tradicionales vs. ML-enhanced (2026)
# Comparative Honeypot Benchmark 2026

**Autor:** Dr. Giovanni Carlos Lorusso Montiel  
**Afiliación:** Universidad Centro Panamericano de Estudios Superiores (UNICEPES), México  
**ORCID:** 0000-0002-3122-8142  
**Email:** al6391@unicepes.edu.mx  
**DOI del Dataset:** https://doi.org/10.5281/zenodo.17688916  

## Descripción
Repositorio para el benchmark comparativo de honeypots tradicionales vs. mejorados con aprendizaje automático. Incluye scripts de despliegue (Docker + Ansible), código original (Cowrie + Isolation Forest) y configuración para 60 días de exposición real.

## Estructura
- `honeypots/`: Docker Compose para cada honeypot.
- `deploy-honeypots.yml`: Playbook Ansible para despliegue.
- `inventory.ini`: IPs reales de las máquinas.

## Uso Rápido
1. Edita `inventory.ini` con tus IPs.
2. `ansible-playbook -i inventory.ini deploy-honeypots.yml`

## Licencia
MIT License – Para tesis postdoctoral y publicaciones académicas.
