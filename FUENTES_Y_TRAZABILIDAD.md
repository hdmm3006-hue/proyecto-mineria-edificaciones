# Registro de procedencia y alcance
Autor: Henry David Muñoz Molina.

## 1. Base propia analizada
Archivo: data/08_dataset_simplificado.csv. Entregado por el autor para este proyecto.
Declaración del autor: base de elaboración propia que reúne varias fuentes, incluidas algunas del DANE, y que no está publicada.
Identidad de bytes: SHA-256 en results/summary.json.
Transformaciones ejecutadas: analysis.py, con resultados y salidas en el notebook.
No se recibieron fuentes originales, reglas de generación ni correspondencia por registro. No se atribuyen sus filas al DANE ni se presupone que cada fila sea un edificio observado. El análisis conserva este alcance de conjunto construido.
Las columnas de cumplimiento y potencial no cuentan con definición de construcción verificable. Potencial no participa en el ajuste. Cumplimiento tiene una prueba adicional de exclusión; la partición no cambia al retirarlo.

## 2. Fuente externa efectivamente consumida
Entidad: Unidad Administrativa Especial de Catastro Distrital (UAECD).
Capa: Construcción de Bogotá.
Servicio: https://sig.catastrobogota.gov.co/arcgis/rest/services/catastro/construccion/MapServer/0
Operación: consulta de conteos agrupados por CONNPISOS sobre OBJECTID, sin geometrías.
Registro de procedencia: data/external/provenance.json (URL, parámetros, fecha UTC, estado HTTP y SHA-256).
Respuesta original: data/external/catastro_pisos_response.json.
Tabla derivada: data/external/catastro_frecuencia_pisos.csv.
Script: external_data.py. Sin --refresh reproduce el snapshot; con --refresh consulta el servicio.
Unidad: elemento de capa catastral; no se asume equivalencia uno a uno con edificios independientes.
Uso: contraste descriptivo de la distribución por pisos. No se unen filas individuales con la base propia.
Atribución: UAECD. No se asigna una licencia de reutilización no verificada.

## 3. Referencias consultadas
CEED-DANE y SGC se usan como referencias documentales/candidatas de futuras integraciones, sin afirmar que sus datos ya estén integrados. Enlaces y alcance en FUENTES_OFICIALES_RECOMENDADAS.md.

## 4. Límite de inferencia
Ninguna consulta externa aquí implementada certifica el cumplimiento sismorresistente de un inmueble ni valida retrospectivamente las decisiones de creación de la base propia. Comparar distribuciones con cobertura diferente no permite extrapolaciones poblacionales ni juicios individuales de seguridad.
