# Proyecto integrador — Minería de Datos
**Autor único: Henry David Muñoz Molina**  
Universidad Santo Tomás, Seccional Tunja · Ingeniería de Datos e Inteligencia Artificial

## Contenido
- report/Informe_IEEE.pdf: reporte en inglés y formato IEEE, con problema, ODS, arquitectura, método, resultados y referencias.
- Proyecto_Mineria_Completo.ipynb: nueve etapas ejecutadas con código, salidas y gráficas.
- analysis.py: limpieza, EDA, selección de k, estabilidad y perfiles.
- external_data.py: consumo real de API oficial y contraste descriptivo.
- data/: original, limpio, segmentado y respuesta externa trazable.
- results/ y figures/: evidencia exportada.
- CHECKLIST_ENTREGA.md: correspondencia con todos los requisitos suministrados.

## Reproducir todo
Entorno probado: Python 3.12; versiones exactas en requirements.txt y results/environment.json.
```bash
python -m pip install -r requirements.txt
python run_all.py
```
run_all.py establece el directorio del proyecto automáticamente. La réplica usa la respuesta externa archivada, comprueba su hash y no necesita red después de instalar dependencias.
Para actualizar únicamente la consulta oficial:
```bash
python external_data.py --refresh
```
Esto sustituye el snapshot y manifiesto por una nueva consulta. El servicio puede cambiar y producir cifras distintas; no mezclar esas cifras con un PDF de una ejecución anterior sin regenerar y revisar el reporte.

## Notebook y Colab
En Jupyter, abrir el notebook desde esta carpeta y ejecutar todas las celdas. Para Colab, subir el ZIP y ejecutar:
```python
from google.colab import files
uploaded = files.upload()
import zipfile, os
with zipfile.ZipFile(next(iter(uploaded))) as z:
    z.extractall('/content/proyecto')
os.chdir('/content/proyecto/entrega_mineria')
!pip -q install -r requirements.txt
!python run_all.py
```
Si Colab pide reiniciar el entorno por paquetes previamente importados, reiniciar y volver a establecer el directorio de trabajo. Para trabajar celda por celda, subir también el notebook y mantener data/ y external_data.py en su directorio de trabajo.

## Compilar el reporte editable
En una instalación completa de TeX Live o en Overleaf, conservar la carpeta report/ y las figuras relativas:
```bash
cd report
pdflatex -interaction=nonstopmode Informe_IEEE.tex
pdflatex -interaction=nonstopmode Informe_IEEE.tex
```
IEEEtran.cls se incluye con su aviso de licencia original. El PDF está revisado visualmente. El texto del reporte presenta los resultados de la ejecución entregada; no se recalcula automáticamente al compilar LaTeX.

## Alcance de los datos
La base de 15.010 registros fue construida por el autor. No se declara inventario representativo ni seguridad estructural comprobada. El consumo oficial nuevo está documentado en FUENTES_Y_TRAZABILIDAD.md y no demuestra retrospectivamente el origen del CSV propio.
Resultados: k=2, silueta muestral 0,2499; grupos de 9.893 y 5.117 registros, principalmente diferenciados por pisos. Al retirar cumplimiento del ajuste, ARI=1 respecto a la partición original. El contraste catastral es independiente y usa unidades y cobertura distintas.

## Publicación y entrega
1. Usar el repositorio oficial del curso. Subir todo el contenido de esta carpeta y verificar que el docente tenga acceso. El ZIP no sustituye el repositorio solicitado.
2. Adjuntar report/Informe_IEEE.pdf y el enlace del repositorio en el campus.
3. Verificar los archivos abriéndolos desde el repositorio y confirmar el envío del campus.
No se ha publicado ni enviado desde esta sesión. No se asigna una licencia abierta al CSV propio o a terceros sin comprobar permisos.
El avance tiene fecha límite 14/11/2026 a las 23:59 según el documento suministrado; el reporte final del 26/11 exige inglés. Esta entrega cubre los lineamientos recibidos y no presupone otros requisitos finales no compartidos.
