# Fuentes oficiales consultadas y recomendadas
**Autor del trabajo: Henry David Muñoz Molina**  
Consulta: 14 de noviembre de 2026.

Estas fuentes se identificaron durante esta revisión. Son referencias y candidatas de complemento; no se ha demostrado que originaran los 15.010 registros del CSV ni se han integrado sus registros al modelo. La base analizada continúa siendo de elaboración propia.

| Prioridad | Fuente y acceso | Aporte al proyecto | Límite |
|---|---|---|---|
| 1 | [DANE, Censo de Edificaciones — CEED](https://microdatos.dane.gov.co/index.php/catalog/873) · [Microdatos](https://microdatos.dane.gov.co/index.php/catalog/873/get-microdata) · [Diccionario](https://microdatos.dane.gov.co/index.php/catalog/873/data-dictionary/F17?file_name=Estructura+CEED) | DPTO_MPIO, DESTINO2, SIS_CONSTR y NRO_PISOS permiten estudiar ubicación, destino, sistema y pisos. | Describe actividad edificadora; no debe tratarse como inventario de todo el parque antiguo. Licenciamiento no equivale a certificación de sismorresistencia. |
| 2 | [SGC, Mapa de Amenaza Sísmica Nacional](https://srvags.sgc.gov.co/arcgis/rest/services/Amenaza_Sismica/Amenaza_Sismica_Nacional/MapServer) · [Sistema de consulta](https://amenazasismica.sgc.gov.co/) | Contexto territorial de amenaza mediante cartografía oficial. | Una capa de amenaza no verifica cumplimiento de un edificio. Hay que documentar modelo, fecha, parámetro y ubicación. |
| 3 | [UAECD, capa Construcción de Bogotá](https://sig.catastrobogota.gov.co/arcgis/rest/services/catastro/construccion/MapServer/0) | CONCODIGO, CONNPISOS, CONALTURA y geometría permiten un caso geográfico de contraste. Admite consultas JSON/GeoJSON. | Solo Bogotá; no se ha verificado una correspondencia con los IDs ED-XXXXXX de la base propia. |

## Correspondencia de variables: propuesta, no integración ya realizada
| Variable propia | Campo o fuente candidata | Transformación que habría que verificar |
|---|---|---|
| ciudad | CEED: DPTO_MPIO | Decodificar DIVIPOLA y seleccionar municipios exactos; no confundir ciudad con área metropolitana. |
| tipo_edificio | CEED: DESTINO2 | Revisar categorías y tabla explícita de equivalencias. |
| numero_pisos | CEED: NRO_PISOS; Bogotá: CONNPISOS | Confirmar unidades, nulos, periodo y unidad de observación. |
| sistema_estructural | CEED: SIS_CONSTR | Revisar el diccionario: sistema constructivo no siempre equivale exactamente al sistema estructural de la base. |
| amenaza_sismica | Cartografía SGC | Requiere criterio geográfico y clasificación documentados; no convertir automáticamente una intensidad en Baja/Intermedia/Alta. |
| antiguedad | Sin correspondencia suficiente comprobada | No confundir año del censo con año de construcción. |
| cumple_norma_sismorresistente | Sin respaldo directo comprobado | Necesita una fuente o regla original explícita; licencia, edad y ciudad no certifican cumplimiento. |
| potencial_estructura_metalica | Indicador propio por documentar | Especificar fórmula y supuestos; no atribuirlo a una entidad oficial. |
| id_edificacion | Identificador interno | Para unir fuentes hace falta una clave real de correspondencia. |

## Recomendación
Priorizar CEED como referencia de datos constructivos y SGC como referencia territorial. Usar Catastro si se desarrolla un caso específico de Bogotá. Conservar separadas las observaciones externas y la base propia hasta verificar claves, unidades, fechas y reglas de transformación. No unir solo por ciudad filas que representan edificios diferentes.

## Referencias para el informe
DANE, “Censo de Edificaciones — CEED”, catálogo y diccionario de datos, consulta 14/11/2026.
Servicio Geológico Colombiano, “Mapa de Amenaza Sísmica Nacional”, geoservicio, consulta 14/11/2026.
Unidad Administrativa Especial de Catastro Distrital, “Construcción”, capa geográfica de Bogotá, consulta 14/11/2026.
Los enlaces y referencias no prueban procedencia de la base original; deben identificarse como fuentes consultadas para esta revisión.
