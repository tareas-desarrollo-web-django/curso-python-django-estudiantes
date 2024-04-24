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
import lorem
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
    
    def insert(self, filas:list[dict]):
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
        sentencia = f"INSERT INTO {self.nombre_tabla} ({columnas_str}) VALUES ({placeholders})"

        # Ejecutamos la sentencia
        self.ejecutar(sentencia, valores=valores)

    def select(self, columnas:list[str]=None, *, restricciones:dict=None, limite:int=None) -> tuple|None:
        r""" 
        Obtiene datos de la tabla, en particular obtiene las columnas 
        especificada sen la lista 'columnas', si no se especifica nada entonces
        se devolverán todas las columnas de la tabla.

        Para controlar o aplicar filtros a los datos que obtendremos podemos
        usar los siguientes argumentos opcionales:
        - restricciones: un diccionario que mapea nombres de columnas a valores
          y solo se devolverán las filas que conciden con esos valores. Por 
          defecto no se aplican restricciones.
        - limire: cantidad máximo de filas que queremos obtener de entre las que
          cumplen con las restricciones. Por defecto se devuelven todos.

        Las filas se retornarán en una lista donde cada fila es un diccionario
        que mapea nombres de columnas a valores.
        """
        # Si no se especifican columnas, retornaremos todas las columnas de la tabla
        if not columnas:
            columnas = list(self.columnas.keys())
        # Si no se especifican restricciones definimos unas vacías
        if not isinstance(restricciones, dict):
            restricciones = {}
        
        # Los valores que son string deben de ser encomillados con comillas simples (')
        restricciones = self.encomillar_valores(restricciones)
        
        # Preparamos la sentencia
        columnas_str = ', '.join(columnas)
        if restricciones:
            clausula_where = 'WHERE ' + ' AND '.join([f"{c} = {v}" for c,v in restricciones.items()])
        else:
            clausula_where = ''
        clausula_limite = f'LIMIT {limite}' if limite else ''
        sentencia = f"SELECT {columnas_str} from {self.nombre_tabla} {clausula_where} {clausula_limite}"

        # Ejecutamos la sentencia que nos devuelve las filas de valores
        filas = self.ejecutar(sentencia)

        # Si hay filas en la respuesta recordemos que solo vienen los valores en el mismo orden en que las columnas
        # fueron dadas en la sentencia, que viene siendo el orden de 'columnas'. Cada fila de valores la convertimos
        # en un diccionario que mapea el nombre de la columna al valor obtenido.
        if filas is not None:
            # Pack the column values with the column names via a dictionary and apply the 'on_load' functions
            filas = [dict(zip(columnas, fila)) for fila in filas]

        return filas
    
    def delete(self, *, restricciones:dict=None):
        r"""
        Elimina filas de la tabla usando un mecanismo básico de restricciones.

        Para especificar qué filas eliminar, usamos el argumento 'restricciones'
        que es un diccionario que mapea nombres de columnas a valores, solo
        se eliminarán las filas que concuerdan con dichos valores. Por defecto
        se eliminarán todas las filas.
        """
        # Si no se especifican restricciones definimos unas vacías
        if not isinstance(restricciones, dict):
            restricciones = {}
        # Los valores que son string deben de ser encomillados con comillas simples (')
        restricciones = self.encomillar_valores(restricciones)

        # Preparamos la sentencia
        clausula_where = 'WHERE ' + ' AND '.join([f"{c} = {v}" for c,v in restricciones.items()]) if restricciones else ''
        sentencia = f"DELETE FROM {self.nombre_tabla} {clausula_where}"

        self.ejecutar(sentencia)


class TablaActivity(TablaSQLite):
    r""" Tabla para almacenar registros de actividades """
    # Nombre de la tabla
    nombre_tabla = 'activity'
    # Columnas de la tabla
    columnas = {
        'id': {
            'attributes': 'INTEGER PRIMARY KEY',
        },
        # Tiempo de inicio del reporte
        'start_time': {
            'attributes':'TIMESTAMP NOT NULL',
        },
        # Descripción de la actividad
        'activity': {
            'attributes': 'TEXT NOT NULL',
        },
    }


class TablaUser(TablaSQLite):
    r"""
    Table for storing information about local apps, since the path is
    involved, then this table is specific for the PC in use.
    """
    # Nombre de la tabla
    nombre_tabla = 'user'
    columnas = {
        # Nombre del usuario, será usado como parte del primary key
        'name': {
            'pk': True,
            'attributes': 'TEXT',
        },
        # Apellido del usuario, será usado como parte del primary key
        'lastname': {
            'pk': True,
            'attributes': 'TEXT',
        },
        # Role del usuario
        'role': {
            'attributes': 'TEXT',
        },
    }


if __name__ == "__main__":
    # Generamos las tablas en la misma base de datos
    tabla_user = TablaUser('bd.sqlite')
    tabla_activity = TablaActivity('bd.sqlite')

    # Nos aseguramos de comenzar un tablas vacías
    tabla_user.delete()
    tabla_activity.delete()

    # Revisamos el contenido de las tablas
    print("Tabla user:")
    print(tabla_user.select())
    print("Tabla activity:")
    print(tabla_activity.select())

    # Insertamos datos a la tabla user, recordemos que las filas tienen que ir en una lista aunque sea una sola
    # NOTA: si el mismo nombre y apellido ya existen recibiremos un error de 'UNIQUE constraint failed'
    # ya que ambos conforman el primary key.
    tabla_user.insert([{'name':'Marcos', 'lastname':'vargas', 'role':'Profesor'}])
    for _ in range(5):
        name = lorem.sentence().split()[0]
        lastname = lorem.sentence().split()[0]
        role = lorem.sentence().split()[0]
        tabla_user.insert([{'name':name, 'lastname':lastname, 'role':role}])

    # Insertamos datos a la tabla activity, recordemos que las filas tienen que ir en una lista aunque sea una sola
    for _ in range(5):
        start_time = datetime.now()
        activity = lorem.sentence()
        tabla_activity.insert([{'start_time':start_time, 'activity':activity}])

    # Revisamos el contenido de las tablas
    print("Tabla user:")
    print(tabla_user.select())
    print("Tabla activity:")
    print(tabla_activity.select())

    # Seleccionamos alguna fila en particular
    print("Fila Marcos:")
    print(tabla_user.select(restricciones={'name':'Marcos'}))

    # Eliminamos una fila en particular
    tabla_user.delete(restricciones={'name':'Marcos'})
    print("Fila Marcos eliminada:")
    print(tabla_user.select())

    # Eliminamos todas las filas de las tablas
    tabla_user.delete()
    tabla_activity.delete()

    # Revisamos el contenido de las tablas
    print("Tabla user:")
    print(tabla_user.select())
    print("Tabla activity:")
    print(tabla_activity.select())