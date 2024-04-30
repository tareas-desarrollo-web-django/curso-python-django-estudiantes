from pathlib import Path
import csv
import pdb

from manejador_sqlite.tablas_sqlite import TablaSQLite


def cargar_csv(ruta_csv:str|Path):
    r"""
    Carga un archivo CSV pero retorna cada fila en forma de diccionario
    que mapea el nombre de la columna al valor correspondiente. Todos los
    valores son retornados como texto. Los nombres de las columnas corresponden
    a como están definidas en el archivo CSV.
    """
    # Cargamos las filas en una lista para insertarlas después
    with open(ruta_csv, 'r') as archivo:
        reader = csv.DictReader(archivo)
        return list(reader)

# PROYECTO
def importar_csv(ruta_csv:str|Path, tabla:TablaSQLite, forzar:bool=False):
    r"""
    Recibe la ruta de una tabla CSV `ruta_csv`, también una instancia de una 
    tabla que hereda de `manejador_sqlite.tablas_sqlite.TablaSQLite`, si 
    quieren pueden asumir que es una instancia de la tabla `TablaMarginacion`,
    solo asegúrense de que el arhivo sqlite usado para la tabla sea el que 
    está definido `configuracion.RUTA_BD`. Como la tabla ya es una instancia 
    entonces ya pueden usar directamente el método `tabla.insert`.

    * La función debe de leer las filas del arhivo csv especificado en `ruta_csv` 
    y meterlas en la tabla especificada en `tabla`.
    Pistas: No olviden usar la función anterior que ya está imlementada `cargar_csv`. 
    Al usar el método insert aunque los valores vayan todos como `str` SQLite 
    los convierte automáticamente al tipo de dato asociado a la columna, por 
    lo que no hay que preocuparse por convertirlos.

    * Los datos se deben de importar solo si no se han importado anteriormente, 
    para garantizar esto una vez importados los datos se debe de crear un 
    archivo en la carpeta especificada por `configuracion.RUTA_DATOS_PROGRAMA`, 
    con el nombre que quieran aunque sea vacío, el hecho de que exista 
    significará que los datos ya fueron importados. Como consecuencia de esto, 
    antes de comenzar a importar los datos debemos revisar si este archivo 
    existe, si ya existe entonces la función debe mostrar el mensaje `"Datos 
    ya importados, no se importarán. Usar 'forzar=True' para forzar la 
    importación"` y retornar de la función.
    
    * Si el parámetro `forzar` es `True`, entonces los datos se deben importar 
    siempre aunque el archivo indicador exista, eliminando el contenido de la 
    tabla SQLite antes de comenzar la importación. 
    Pistas: usar el método `tabla.delete`.
    """
    print(f"Se debe implementar la función 'importar_csv()'")
    












