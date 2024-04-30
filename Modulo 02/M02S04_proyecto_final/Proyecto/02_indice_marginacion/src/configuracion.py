from pathlib import Path

########################################
# Rutas carpetas y archivos

# Ruta raiz del proyecto
RUTA_BASE = Path(__file__).parent

# Ruta de la carpeta de datos
RUTA_DATOS = RUTA_BASE / 'datos'
# Ruta del CSV de la tabla de marginación
RUTA_CSV_MARGINACION = RUTA_DATOS / 'IML_2020.csv'

# Ruta de la carpeta donde almacenaremos los datos generados por el programa
RUTA_DATOS_PROGRAMA = RUTA_BASE / 'datos_programa'
# Ruta del archivo de la base de datos
RUTA_BD = RUTA_DATOS_PROGRAMA / 'bd.sqlite'





