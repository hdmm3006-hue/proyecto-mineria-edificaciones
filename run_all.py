"""Ejecutar todo desde cualquier carpeta. Autor: Henry David Muñoz Molina."""
from pathlib import Path
import os, runpy
root=Path(__file__).resolve().parent
os.chdir(root)
runpy.run_path(str(root/'analysis.py'),run_name='__main__')
