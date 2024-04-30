r"""
Ejemplo de como usar la herencia para aprovechar código y facilitar la extención
de funcionalidad. 

Esto mediante un ejemplo donde nuestra clase base se encarga de implementar 
todo el manejo de tablas para bases de datos SQLite. Para que la clase funcione
de manera adecuada y generalizada solo requiere conocer el nombre de la tabla y
las columnas que va a contener junto con sus atributos en sitaxis SQLite. Esto
se define en los atributos de clase `nombre_tabla` y `columnas`.

De esta forma, si queremos integrar una tabla nueva a nuestra aplicación solo
tenemos que heredar de la clase base y unicamente definir los atributos de clase
`nombre_tabla` y `columnas`.

NOTA: es un ejemplo y para simplificar el código no se aplica el manejo de 
errores.
"""

import sqlite3
from datetime import datetime


class TablaSQLite:
    r""" Tabla para almacenar registros de actividades """
    # Configuraciones para las subclases
    # Nombre de la tabla
    nombre_tabla = None
    # Columnas de la tabla
    columnas = None

    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self.crear_tabla()
    
    def ejecutar(self, sentencias:str, *, valores:list[tuple]=None):
        r"""
        Ejecuta sentencias en el archivo SQLite. 
        
        El argumento `valores` solo debe ser usado cuando la sentencia tiene 
        placeholders, como 'INSERT INTO user (name, lastname) VALUES (?,?)', 
        de forma que queremos que se ejecute la instrucción varias veces una 
        para cada registro de valores dado. Cada elemento de la lista `valores` 
        debe contener igual número de elementos que los placeholders '?' de 
        la sentencia. Esto solo funciona con sentencias que meten o modifican
        valores.
        """
        # Creamos la conexión con el archivo
        conn = sqlite3.connect(self.ruta_archivo)
        cursor = conn.cursor()

        # Ejecutamos las sentencias
        if valores is None:
            cursor.execute(sentencias)
            filas = cursor.fetchall()
        else:
            cursor.executemany(sentencias, valores)
            filas = []

        # Aplicamos las sentencias a la base de datos
        conn.commit()

        cursor.close()
        conn.close()

        return filas

    def crear_tabla(self):
        r""" 
        Genera el código SQLite para crear la tabla
        """
        # Definiciones de columnas
        columnas_definitiones = ', '.join([f"{c} {p['attributes']}" for c,p in self.columnas.items()])
        # Instrucción para generar los posibles primary keys
        pk_cols = [c for c,p in self.columnas.items() if 'pk' in p and p['pk']]
        primary_keys = f", PRIMARY KEY ({', '.join(pk_cols)})" if pk_cols else ''

        sentencia = f"CREATE TABLE IF NOT EXISTS {self.nombre_tabla} ({columnas_definitiones}{primary_keys})"
        
        self.ejecutar(sentencia)

    def encomillar_valores(self, datos):
        r"""
        Recibe un dicionario que mapea nombres de columnas a valores y retorna
        un diccionario equivalente pero con los valores que son stirngs 
        encomillados con comillas simples (').
        """
        return {c:f"'{v}'" if isinstance(v, str) else v for c,v in datos.items()}
    
    def insert(self, filas:list[dict], *, ignorar_repetidos:bool=True):
        r"""
        Inserta filas en la tabla.

        Debemos dar las filas que vamos a insertar, cada fila debe venir 
        en forma de diccionario donde la llave es el nombre de la columna a la
        que corresponde el valor. Cada fila debe contener al menos las columnas
        requeridas como las PRIMARY KEY, las NOT NULL, etc.
        """
        if not len(filas):
            return
        
        # Obtenemos una lista con las diferentes columnas que aparecen en al menos un registro
        # Esta lista definirá el orden en el que generaremos las tuplas de valores
        columnas = list(set().union(*[set(row.keys()) for row in filas]))
        # Generamos las tuplas de valores para cada registro, en el mismo orden que 'columnas', None para las faltantes
        valores = [tuple(row.get(c, None) for c in columnas) for row in filas]

        # Generamos la sentencia
        columnas_str = ', '.join(columnas)
        placeholders = ', '.join(('?',) * len(columnas))
        clausula_ignore = 'OR IGNORE' if ignorar_repetidos else ''
        sentencia = f"INSERT {clausula_ignore} INTO {self.nombre_tabla} ({columnas_str}) VALUES ({placeholders})"

        # Ejecutamos la sentencia
        self.ejecutar(sentencia, valores=valores)

    def select(self, columnas:list[str]=None, *, where:dict=None, limit:int=None) -> tuple|None:
        r""" 
        Obtiene datos de la tabla, en particular obtiene las columnas 
        especificada sen la lista 'columnas', si no se especifica nada entonces
        se devolverán todas las columnas de la tabla.

        Para controlar o aplicar filtros a los datos que obtendremos podemos
        usar los siguientes argumentos opcionales:
        - where: un diccionario de restricciones que mapea nombres de columnas 
          a valores y solo se devolverán las filas que conciden con esos 
          valores. Por defecto no se aplican restricciones.
        - limit: cantidad máximo de filas que queremos obtener de entre las que
          cumplen con las restricciones. Por defecto se devuelven todos.

        Las filas se retornarán en una lista donde cada fila es un diccionario
        que mapea nombres de columnas a valores.
        """
        # Si no se especifican columnas, retornaremos todas las columnas de la tabla
        if not columnas:
            columnas = list(self.columnas.keys())
        # Si no se especifican restricciones definimos unas vacías
        if not isinstance(where, dict):
            where = {}
        
        # Los valores que son string deben de ser encomillados con comillas simples (')
        where = self.encomillar_valores(where)
        
        # Preparamos la sentencia
        columnas_str = ', '.join(columnas)
        if where:
            clausula_where = 'WHERE ' + ' AND '.join([f"{c} = {v}" for c,v in where.items()])
        else:
            clausula_where = ''
        clausula_limit = f'LIMIT {limit}' if limit else ''
        sentencia = f"SELECT {columnas_str} from {self.nombre_tabla} {clausula_where} {clausula_limit}"

        # Ejecutamos la sentencia que nos devuelve las filas de valores
        filas = self.ejecutar(sentencia)

        # Si hay filas en la respuesta recordemos que solo vienen los valores en el mismo orden en que las columnas
        # fueron dadas en la sentencia, que viene siendo el orden de 'columnas'. Cada fila de valores la convertimos
        # en un diccionario que mapea el nombre de la columna al valor obtenido.
        if filas is not None:
            # Pack the column values with the column names via a dictionary and apply the 'on_load' functions
            filas = [dict(zip(columnas, fila)) for fila in filas]

        return filas
    
    def select_distinct(self, columnas:list[str], *, where:dict=None):
        r"""
        Retorna una lista con las diferentes tuplas formadas por los valores
        de las columnas especificadas en `columnas`. Además podemos imponer
        restricciones mediante el atributo `where` que mapea nombres
        de columnas a valores.
        """
        # Si no se especifican restricciones definimos unas vacías
        if not isinstance(where, dict):
            where = {}
        
        # Los valores que son string deben de ser encomillados con comillas simples (')
        where = self.encomillar_valores(where)

        # Preparamos la sentencia
        columnas_str = ', '.join(columnas)
        if where:
            clausula_where = 'WHERE ' + ' AND '.join([f"{c} = {v}" for c,v in where.items()])
        else:
            clausula_where = ''
        
        sentencia = f"SELECT DISTINCT {columnas_str} from {self.nombre_tabla} {clausula_where}"
        
        filas = self.ejecutar(sentencia)
        
        return filas

    def delete(self, *, where:dict=None):
        r"""
        Elimina filas de la tabla usando un mecanismo básico de restricciones.

        Para especificar qué filas eliminar, usamos el argumento 'where'
        que es un diccionario que mapea nombres de columnas a valores, solo
        se eliminarán las filas que concuerdan con dichos valores. Por defecto
        se eliminarán todas las filas.
        """
        # Si no se especifican restricciones definimos unas vacías
        if not isinstance(where, dict):
            where = {}
        # Los valores que son string deben de ser encomillados con comillas simples (')
        where = self.encomillar_valores(where)

        # Preparamos la sentencia
        clausula_where = 'WHERE ' + ' AND '.join([f"{c} = {v}" for c,v in where.items()]) if where else ''
        sentencia = f"DELETE FROM {self.nombre_tabla} {clausula_where}"

        self.ejecutar(sentencia)

