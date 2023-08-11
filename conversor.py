"""
Conversor de pdf a excel se esta usando la libreria  de camelot, es importante tener en cuenta lo siguiente, esta libreria usa pypdf de una version atrasada por lo cual 
esto puede causar ciertos conflictos, para evitar lo mismo recomiendo usar esto en un entorno virtual de su preferencia (venv o conda), para evitar conflictos en proyectos futuros,
para poder usar este escript se uso lo siguiente:
!pip install "camelot-py[cv]" -q
!pip install PyPDF2==1.26.0

Se usaron otras librerias pyplumber, tabula pero camelot fue la mas efectiva para hacer esta tarea en concreto

Por el momento se esperan mas pdf para hacer mas pruebas sobre este script
"""
import camelot
import pandas as pd

# Lee todas las tablas de todas las páginas
tables = camelot.read_pdf('colocar la ruta del archivo', pages='all', flavor="stream")

# Combina todas las tablas en un solo DataFrame
all_tables_df = pd.concat([table.df for table in tables])

# Guarda el DataFrame combinado en un archivo Excel
all_tables_df.to_excel('colocar la direccion a exportar seguido del nombre del archivo.xlsx', index=False)