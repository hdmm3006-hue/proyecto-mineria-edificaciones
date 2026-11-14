# Matriz de cumplimiento — Minería de Datos
Autor: Henry David Muñoz Molina. Alcance: lineamientos del avance entregados por el usuario.

| Requisito | Evidencia concreta | Estado |
|---|---|---|
| Reporte técnico IEEE | report/Informe_IEEE.pdf y fuente .tex | Preparado, en inglés |
| Introducción y problema | Secciones I–II del reporte | Incluido |
| Vinculación con ODS | ODS 11 y meta 11.5, alcance conceptual explícito | Incluido |
| Estructura general del sistema | Diagrama y sección IV del reporte | Incluido |
| Dataset estructurado y limpio | CSV original y limpio; categorías verificadas | Ejecutado |
| Nulos y duplicados | Auditoría de valores vacíos, nulos, filas e IDs | Ejecutado: sin nulos ni duplicados detectados |
| Manejo de atípicos | 267 casos listados; conservación justificada y prueba de recorte | Ejecutado; no se inventa validación de campo |
| EDA profundo | Distribuciones, estadísticas, cruces, tasas, asociaciones y contraste externo | Ejecutado |
| Clustering o asociación | K-Means con k=2..8; codificación y distancia documentadas | Ejecutado |
| Evaluación e interpretación | Silueta, DB, CH, perfiles, semillas y tres sensibilidades | Ejecutado |
| Fuentes externas (opcional) | external_data.py, respuesta oficial, manifiesto y comparación | Ejecutado mediante API REST |
| Código reproducible | run_all.py, requirements, notebook ejecutado y snapshot | Ejecutado desde archivos guardados |
| Bibliografía | ONU, scikit-learn, DANE, SGC, Catastro y lineamientos | Incluida; función de cada fuente delimitada |
| Autoría | Henry David Muñoz Molina | Único autor del entregable |
| Cloud | No cursada | No aplica |
| Subida a GitHub/GitLab oficial | Archivos e instrucciones preparados | Requiere URL del repositorio y acceso |
| Envío al campus | PDF y ZIP preparados | No enviado |

## Alcance de la afirmación de cumplimiento
Los componentes técnicos solicitados están desarrollados y documentados. No se afirma que la entrega institucional ya haya ocurrido ni se garantiza una calificación. La base propia se analiza como conjunto construido: su trazabilidad histórica no está verificada, y sus resultados no se generalizan a edificios reales. La consulta oficial nueva tiene trazabilidad completa y no se usa para atribuir retroactivamente un origen a la base propia. Las restricciones se presentan como limitaciones metodológicas, no se ocultan ni se completan con datos inventados.
