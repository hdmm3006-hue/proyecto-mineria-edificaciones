# Cómo explicar el proyecto

**Problema:** organizar una base propia de edificaciones y descubrir perfiles con minería no supervisada. Se relaciona con el ODS 11, sin afirmar que mide directamente un indicador del ODS.

**Limpieza:** comprobamos las 15.010 filas, categorías, identificadores y pisos. No había nulos ni duplicados; no inventamos problemas para aplicar técnicas. Los 267 edificios de más de 50 pisos se marcaron, no se declararon errores ni se verificaron como reales.

**EDA:** encontramos que ciudad y amenaza casi determinan la misma información y que el cumplimiento está concentrado en dos ciudades. Esto obliga a revisar cómo se integraron las fuentes. No demuestra que las otras ciudades sean inseguras.

**Codificación:** one-hot representa categorías con columnas binarias. No usamos números arbitrarios para materiales ni convertimos intervalos de antigüedad en años exactos. Estandarizamos pisos para evitar que su escala original dominara sin control; además probamos cambiar su peso.

**K-Means:** asigna filas a centroides cercanos, recalcula promedios y repite. Probamos de 2 a 8 grupos; seleccionamos 2 por la mejor silueta de la comparación. La silueta de 0,2499 no significa 24,99 % de precisión: mide cohesión y separación, y aquí la separación es limitada.

**Resultado:** un grupo tiene 9.893 filas y promedio de 13 pisos; el otro, 5.117 y promedio de 32,25. No podemos llamarlos seguros/inseguros. La altura es la principal diferencia.

**Validación:** semillas diferentes y recorte IQR produjeron la misma asignación (ARI=1); al reducir el peso de pisos la concordancia fue 0,9221. ARI tampoco mide seguridad ni exactitud frente a una verdad externa.

**Limitación:** la base fue construida por el equipo a partir de varias fuentes. Debemos identificar cuáles y cómo transformamos información agregada o individual. No se atribuye la totalidad de la base al DANE.

**Qué cambió frente al PDF anterior:** se sustituyeron 290 casos y cinco grupos ilustrativos por resultados calculados con las 15.010 filas reales del archivo. “Reales del archivo” no significa observaciones verificadas de edificios reales.

**Fuente externa ejecutada:** consultamos la API de Catastro Bogotá y guardamos la respuesta agregada, fecha, parámetros y hash. La reproducción puede hacerse sin conexión. Se comparan distribuciones de pisos, sin unir edificios ni suponer la misma cobertura. El contraste confirma que nuestra base de edificios altos no representa automáticamente toda la capa catastral.

**Prueba adicional:** al quitar la variable de cumplimiento, la asignación de los dos grupos se conserva. Esto reduce la dependencia del resultado respecto a esa columna, pero no prueba que sus valores sean correctos.
