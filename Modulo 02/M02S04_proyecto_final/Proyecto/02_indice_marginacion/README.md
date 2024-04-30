Análisis del Índice de Marginación
==============================================

El objetivo de este proyecto es explorar la Programación Orientada a Objetos implementando un programa para realizar un pequeño análisis del índice de marginación de las localidades del país, proporcionado por INEGI, mediante un generador de gráficas.

Se pretende que practiquen la implementación de sus propias clases pero también que practiquen el usar clases ya existentes, por eso yo les proporcionaré algo de código listo para ser usado mediante clases. También les voy a diseñar la estructura y organización que debe llevar el proyecto precisamente para garantizar el uso de lo que vimos en clases, ustedes solo deben implementar los métodos que les indicaré más adelante. 

Al momento de implementar, es posible que ustedes necesiten importar lo necesario de de los componentes que ya están implementados así como de las librerías que quieran utilizar en su implementación.

Yo les doy algunas pistas, pero recuerden que pueden implementar las cosas como ustedes gusten y usar las librerías y herramientas que ustedes quieran.

Para que funcionen los componentes que ya les doy implementados es necesario instalar lo siguiente:
* `pip install seaborn`
* `pip install pandas`


## Estructura del proyecto

### Módulos que ya están implementados

* `datos`: carpeta normal con los datos que usará la aplicación, solo son dos archivos:
    * `IML_2020.csv`: la tabla del índice de marginación descargada de INEGI. Cada fila corresponde a una localidad del país, la lista de coulmnas completa se puede revisar en el archivo `Descripcion de datos.txt`. La columna más importante es `GM_2020` que contiene el grupo de marginación al que pertenece cada localidad `Muy bajo, Bajo, Medio, Alto, Muy alto`. **Mientras mayor sea la marginación, significa que la localidad es de más bajos recursos**.
    * `Descripcion de datos.txt`: archivo de texto que describe las columnas de la tabla anterior.

* `manejador_sqlite`: paquete para manejar tablas SQLite como vimos en clase, solo contiene dos módulos:
    * `tablas_sqlite.py`: implementa la clase base `TablaSQLite` que incorpora toda la funcionalidad para guardar y sacar datos de la tabla. como vimos en clase, para que una tabla sea funcional solo se necesita heredar de esta clase y definir el nombre de la tabla y las columnas. Para el proyecto no es necesario implementar nada en este módulo.
    * `tablas.py`: implementa la tabla SQlite `TablaMarginacion` que hereda de `TablaSQLite` y contiene las mismas columnas que el archivo de datos `IML_2020.csv`. La idea es usar esta tabla para importar los datos del archivo a esta tabla SQLite. Para el proyecto no es necesario implementar nada en este módulo. Los métodos principales son los siguientes:
        * Para interactuar con la tabla tenemos que crear una instancia de `TablaMarginacion` pasándole como parámetro la ruta del archivo `sqlite` que almacena la tabla, como vimos en clases:
            ```python
            tabla = TablaMarginacion(ruta_sqlite)
            ```
        * `insert`: recibe una lista de registros en `filas` donde cada registro es un diccionario que mapea nombres de columnas a valores e inserta los registros en la tabla SQLite. Si la llave primaria ya existe entonces el registro se ignorará por defecto, a menos que especifiquemos el parámetro `ignorar_repetidos=False`, con lo cual se arrojará un error si ya existe alguna de las llaves primarias en la tabla:
            ```python
            tabla.insert(filas:list[dict], *, ignorar_repetidos:bool=True)
            ```
        * `select`: obtiene registros de la tabla directamente de la base de datos, por defecto obtiene todos los registros, pero podemos especificar que solo nos devuelva algunas de las columnas especificando los nombres en el parámetro `columnas`, además podemos especificar unas restricciones mediante el parámetro `where` que debe ser un diccinario que mapea nombres de columnas al valor que queremos que cumplan los registros que obtendremos. Adeás, mediante el parámetro `limit` podemos especificar un entero para que solo no retorne esa cantidad de registros como máximo. El resutado es una lista de diccionarios igual a como se pasan los datos a `select`:
            ```python
            tabla.select(columnas:list[str]=None, *, where:dict=None, limit:int=None)
            ```
        * `select_distinct`: similar a `select`, pero en este caso nos devuelve solo los valores distintos conformados por las columnas especificadas. Podemos especificar también restricciones mediante el parámetro `where`. El resultado es una lista de tuplas que contiene las distintas tuplas conformadas por los registros que cumplen con las restricciones:
            ```python
            tabla.select_distinct(columnas:list[str], *, where:dict=None)
            ```
        * `delete`: elimina registros de la tabla, por defecto elimina todos los datos pero podemos especificar restricciones en el parámetro `where` para que solo se eliminen los registros que cumplan con esos valores.
            ```python
            tabla.delete(where:dict=None)
            ```

* `configuracion.py`: un módulo de configuraciones donde están definidas las rutas principales como lo son la ruta base del proyecto `RUTA_BASE` que corresponde a la carpeta `src`, la ruta de la carpeta de datos `RUTA_DATOS`, la ruta del csv de la tabla de marginación `RUTA_CSV_MARGINACION`, una ruta donde se deben almacenar todos los archivos generados por el programa `RUTA_DATOS_PROGRAMA` y la ruta del archivo SQLite donde se trabajará nuestra base de datos. Para el proyecto no es necesario implementar nada en este módulo, pero si quieren agregar sus propias configuraciones pueden hacerlo. Hay que revisar el módulo para saber bien lo que contiene, las rutas están definidas con `Path`, recuerden que si quieren la ruta en texto solo tiene que usar la función `str`.

* `graficador.py`: módulo con funciones para generar los gráficos que serán manejados por la aplicación, las funciones ya están listas para usarse y no necesitan implementar nada en este módulo, solo hay que hacer uso de las funciones. Las funciones son las siguientes:
    * `grafico_por_pares`: recibe en `datos` una lista de registros de la tabla de Marginación `TablaMarginacion` tal cual como los devuelve el método `select` de la tabla, además recibe parejas de nombres de columnas y genera en una misma ventana una gráfica para cada pareja de columnas dada. Los nombres de las columnas deben ser especificados como están en la tabla:
        ```python
        grafico_por_pares(datos:list[dict], pares:list[tuple])
        ```
    * `grafico_por_pares_producto`: recibe en `datos` una lista de registros de la tabla de Marginación `TablaMarginacion` tal cual como los devuelve el método `select` de la tabla, además recibe una lista de columnas para el eje `x` y una lista de columnas para el eje `y` y genera una matriz de gráficos con todas las combinaciones entre columnas de `x` y columnas de `y`. Los nombres de las columnas deben ser especificados como están en la tabla:
        ```python
        grafico_por_pares_producto(datos:list[dict], columnas_x:list[str], columnas_y:list[str])
        ```
    * `grafico_barras_acumulado`: recibe en `datos` una lista de registros de la tabla de Marginación `TablaMarginacion` tal cual como los devuelve el método `select` de la tabla y genera un gráfico de barras acumulado que muestra para cada región el porcentaje de localidades en cada grupo de marginación, las regiones dependen de los datos, si los datos contienen registros solamente de un estado entonces las regiones serán los municipios del estado, pero si hay registros de más de un estado entonces
    las regiones serán los estados:
        ```python
        grafico_barras_acumulado(datos:list[dict])
        ```

### Módulos que hay que implementar

* `importar_datos.py`: módulo con las funciones necesarias para importar los datos que están en la tabla `datos/IML_2020.csv` hacia la tabla SQLite definida en `manejador_sqlite.tablas.TablaMarginacion`. Contiene las funciones siguientes:
    * `cargar_csv(ruta_csv:str|Path)`: **esta función ya está implementada**, recibe la ruta de un archivo CSV, lo lee y devuelve una lista con las filas del archivo, cada fila en un diccionario que mapea nombres de columnas a valores, todos los valores retornados estarán como `str`.
    * `importar_datos(ruta_csv:str|Path, tabla:TablaMarginacion, forzar:bool=False)`: **esta función se debe implementar** con los siguientes requerimientos:
        * Recibe la ruta de una tabla CSV `ruta_csv`, también una instancia de una tabla que hereda de `manejador_sqlite.tablas_sqlite.TablaSQLite`, si quieren pueden asumir que es una instancia de la tabla `TablaMarginacion`, solo asegúrense de que el arhivo sqlite usado para la tabla sea el que está definido `configuracion.RUTA_BD`. Como la tabla ya es una instancia entonces ya pueden usar directamente el método `tabla.insert`.
        * La función debe de leer las filas del arhivo csv especificado en `ruta_csv` y meterlas en la tabla especificada en `tabla`. 
            * **Pistas**: no olviden usar la función anterior que ya está imlementada `cargar_csv`. Al usar el método insert aunque los valores vayan todos como `str` SQLite los convierte automáticamente al tipo de dato asociado a la columna, por lo que no hay que preocuparse por convertirlos.
        * Los datos se deben de importar solo si no se han importado anteriormente, para garantizar esto una vez importados los datos se debe de crear un archivo en la carpeta especificada por `configuracion.RUTA_DATOS_PROGRAMA`, con el nombre que quieran aunque sea vacío, el hecho de que exista significará que los datos ya fueron importados. Como consecuencia de esto, antes de comenzar a importar los datos debemos revisar si este archivo existe, si ya existe entonces la función debe mostrar el mensaje `"Datos ya importados, no se importarán. Usar 'forzar=True' para forzar la importación"` y retornar de la función.
        * Si el parámetro `forzar` es `True`, entonces los datos se deben importar siempre aunque el archivo indicador exista, eliminando el contenido de la tabla SQLite antes de comenzar la importación. 
            * **Pistas**: usar el método `tabla.delete`.
        * `Nota`: pueden confirmar si los datos fueron importados correctamente con instrucciones similares a las siguientes, el número de filas debe ser `108144`:
            ```python
            from manejador_sqlite.tablas import TablaMarginacion
            from importar_datos import importar_csv
            import configuracion
            >>> tabla = TablaMarginacion(configuracion.RUTA_BD)
            >>> importar_csv(configuracion.RUTA_CSV_MARGINACION, tabla)
            >>> filas = tabla.select()
            >>> print(len(filas))
            108144
            >>> print(filas[0])
            {'CVE_LOC': '010010001', 'ENT': '01', 'NOM_ENT': 'Aguascalientes', 'MUN': '001', 'NOM_MUN': 'Aguascalientes', 'LOC': '0001', 'NOM_LOC': 'Aguascalientes', 'POB_TOT': 863893, 'ANALF': 1.429923686, 'SBASC': 19.16481924, 'OVSDE': 0.014187218, 'OVSEE': 0.079424608, 'OVSAE': 0.129196563, 'OVPT': 0.453217003, 'OVHAC': 14.46777187, 'OVSREF': 3.531759553, 'IM_2020': 24.96229212, 'GM_2020': 'Muy bajo', 'IMN_2020': 0.953434799}
            ```

* `app.py`: módulo principal que contiene la lógica de la aplicación que será implementada haciendo uso de todo lo anterior. Contiene una clase llamada `App`, algunos de los métodos ya están implementados y el resto deben ser implementados como parte del proyecto. 
    * Los métodos implementados son los sigiuentes:
        * `__init__(self)`: **el constructor de la clase ya está implementado** con la inicialización necesaria. Realiza lo siguiente:
            * Inicializa los atributos `cols_numeracion` y `estados` a `None` para que su contenido sea generado por otros métodos.
            * Inicializa el atributo `tabla_marginacion` como una instancia de la tabla `TablaMarginacion`, así podemos interactuar con la tabla de marginación dentro de la clase mediante este atributo.
            * Invoca los métodos que inicializan los atributos previos, lo cual será discutido en los métodos correspondientes.
        * `_generar_estados(self)`: **este método ya está implementado**, al ejecutar este método la tabla en `self.tabla_marginacion` debió importar los datos de marginación. Este método genera el contenido del atributo `self.estados` que es una diccionario con los distintos estados que aparecen en la tabla de marginación. El diccionario mapea la clave del estado como está dada en la columna 'ENT' de la tabla al nombre del estado como está en la columna `NOM_ENT`. Los datos no son retornados sino que son asignados al atributo `self.estados`. Los datos son los siguientes:
        `{'01': 'Aguascalientes', '02': 'Baja California', ...}`

    * Los métodos que hay que implementar son los siguientes:
        * `_generar_numeracion_columnas(self)`: Usar la tabla `TablaMarginacion` para generar un diccionario que asigna a cada una de sus columnas columna un índice comenzando desde uno. El diccionario debe mapear el índice asignado a una tupla que contenga el nombre de la columna y el descriptivo, tal cual están registrados en la tabla `TablaMarginacion`, pero solo deben estar las columnas que estén registradas de tipo REAL o INTEGER. Hay que revisar el código de la clase `TablaMarginacion` para decidir como implementar eso. El diccionario generado debe ser como el siguiente ejemplo, pero no debe ser retornado sino que debe ser asignado al atributo `self.cols_numeracion`:
            ```python
            {
                1: ('POB_TOT', 'Población total'),
                2: ('ANALF', 'Porcentaje analfabeta'),
                3: ('SBASC', 'Porcentaje sin educación básica'),
                ...
                11: ('IMN_2020', 'Índice de marginación normalizado')
            }
            ```
            * PISTAS:
                * El orden de la numeración no importa, solo que unicamente estén las columnas REAL o INTEGER.
                * Hacer uso del atributo `TablaMarginacion.columnas`.
                * Para saber si una columna es REAL solo debemos revisar si 'real'
                está en la versión en minúsculas de la propiedad 'attributes' de la 
                columna y similar para saber si es INTEGER.
        
        * `menu_principal(self)`: este método debe mostrar en la terminal un menú y al mismo tiempo debe solicitar al usuario que ingrese una opción. Si la opción ingresada no es válida se debe mostrar el mensaje '> Opción no válida' y debe pedir la opción de nuevo sin mostrar el menú otra vez, como en el siguiente ejemplo. Mostrar una pequeña fila de arteriscos al inicio. La opción ingresada final se debe retornar como un entero::
            ```bash
            ****************************************
                        Menú principal
            1 - Graficas por pares
            2 - Gráficas por matriz
            3 - Marginación por territorio
            4 - Salir del programa
            > Ingresa número de opción: a
            > Opción no válida
            > Ingresa número de opción: 9
            > Opción no válida
            > Ingresa número de opción: 2
            2
            ```
            * Pistas:
                * Al convertir a entero con `int` si el valor no es convertible se arroja una excepción de tipo `ValueError`, podemos complementar arrojando nosotros un `raise ValueError()` si la opción sí es entera pero no está en el rango del menú. Podríamos aprovechar esto con un bloque `try ... except`.
        
        * `mostrar_columnas_numericas(self)`: este método debe mostrar una lista estilo menú con los descriptivos de las columnas almacenadas en el atributo `self.cols_numeracion` que fue generado con el método `self._generar_numeracion_columnas`. El orden de la numeración debe ser idéntica a como está definida en el atributo `self.cols_numeracion`, en este caso no debe solicitar ninguna opción, ya que este método será usado por otros métodos que sí solicitan entrada en base a esta lista. La lista debe verse como el siguiente:
            ```bash
            Columnas disponibles:
            1 - Población total
            2 - Porcentaje analfabeta
            3 - Porcentaje sin educación básica
            4 - Porcentaje sin drenaje ni excusado
            5 - Porcentaje sin electricidad
            6 - Porcentaje sin agua
            7 - Porcentaje con piso de tierra
            8 - Porcentaje con hacinamiento
            9 - Porcentaje sin refrigerador
            10 - Índice de marginación
            11 - Índice de marginación normalizado
            ```
        
        * `mostrar_estados(self)`: este método debe mostrar una lista estilo menú con los estados almacenados en el atributo `self.estados`, además, al inicio de la lista debe estar la opción `00 - Todos`, usamos la clave `00` porque esa no corresponde a ningún estado. No debe solicitar ninguna opción, ya que este método será usado por otros métodos que sí solicitan entrada en base a esta lista. La lista debe verse como el siguiente ejemplo:
            ```bash
            Estados disponibles:
            00 - Todos
            01 - Aguascalientes
            02 - Baja California
            03 - Baja California Sur
            04 - Campeche
            05 - Coahuila de Zaragoza
            06 - Colima
            ...
            32 - Zacatecas
            ```
        
        * `menu_secundario_graficas_pares(self)`: Este método debe mostrar el menú correspondiente a la funcionalidad de `Gráficas por pares` del menú principal. 
            * Al inicio debe mostrar una pequeña fila de arteriscos seguido del texto `Gráficas por pares`.
            * La lista de opciones debe ser la que despliega el método `self.mostrar_columnas_numericas`, es decir, la numeración de las columnas numéricas junto con los descriptivos. 
            * Al mismo tiempo debe solicitar que el usuario ingrese parejas de columnas mediante los números asignados a cada columna en la lista. Las parejas deben ser ingresadas en la forma `1:3, 2:4, 3:5`, los espacios no deben importar.
            * Si la lista ingresada no es válida, ya sea porque un valor no es entero o está fuera del rango de la lista entonces se debe mostrar el mensaje `> Opción no válida` y debe pedir las parejas de nuevo sin mostrar el menú otra vez.
            * Las parejas ingresadas se deben retornar pero como nombres de columnas de la tabla de marginación en correspondencia con el menú, es decir, si el usuario ingresa '1:3, 2:4' se debe retornar `[('POB_TOT', 'SBASC'), ('ANALF', 'OVSDE')]`, porque esos son los nombres de las columnas que corresponden a la numeración.
            * El funcionamiento del menú debe verse como el siguiente ejemplo:
                ```bash
                ****************************************
                        Gráficas por pares
                Columnas disponibles:
                1 - Población total
                2 - Porcentaje analfabeta
                3 - Porcentaje sin educación básica
                4 - Porcentaje sin drenaje ni excusado
                5 - Porcentaje sin electricidad
                6 - Porcentaje sin agua
                7 - Porcentaje con piso de tierra
                8 - Porcentaje con hacinamiento
                9 - Porcentaje sin refrigerador
                10 - Índice de marginación
                11 - Índice de marginación normalizado
                > Ingresa las parejas de la forma '1:3, 2:4, 3:5': a
                > Opción no válida
                > Ingresa las parejas de la forma '1:3, 2:4, 3:5': 1:a 4:3
                > Opción no válida
                > Ingresa las parejas de la forma '1:3, 2:4, 3:5': 1:2, 3:50  
                > Opción fuera de rango: 50
                > Ingresa las parejas de la forma '1:3, 2:4, 3:5': 1:2, 3:4  
                [('POB_TOT', 'ANALF'), ('SBASC', 'OVSDE')]
                ```
            * Pistas:
                * Hacer uso del método `self.mostrar_columnas_numericas()` para desplegar la lista.
                * Hacer uso del atributo `self.cols_numeracion` para recuperar el nombre de las columnas si tenemos la numeración correspondiente.
                * Considerar usar la función `.split` de los `str` para dividir textos de la entrada ingresada.
        
        * `menu_secundario_graficas_matriz`: este método debe mostrar el menú correspondiente a la funcionalidad de `Gráficas por matriz` del menú principal. 
            * Al inicio debe mostrar una pequeña fila de arteriscos seguido del texto `Gráficas por matriz`.
            * La lista de opciones debe ser la que despliega el método `self.mostrar_columnas_numericas`, es decir, la numeración de las columnas numéricas junto con los descriptivos. 
            * Al mismo tiempo debe solicitar que el usuario ingrese dos listas de números de opciones del menú. Las listas deben deben ser ingresadas en la forma `1,3,2 : 4,3`, que representaría a las listas `[1, 3, 2]` y `[4, 3]`, los espacios no deben importar.
            * Si las listas ingresadas no son válidas, ya sea porque un valor no es entero, está fuera del rango del menú o no se dieron 2 listas entonces se debe mostrar el mensaje `> Opción no válida` y debe pedir las dos listas de nuevo sin mostrar el menú otra vez.
            * Las listas ingresadas se deben retornar pero como nombres de columnas de la tabla de marginación en correspondencia con el menú, es decir, si el usuario ingresa `1,2 : 3, 5, 6` se debe retornar `[['POB_TOT', 'ANALF'], ['SBASC', 'OVSEE', 'OVSAE']]`, porque esos son los nombres de las columnas que corresponden a la numeración.
            * El funcionamiento del menú debe verse como el siguiente ejemplo:
                ```bash
                ****************************************
                        Gráficas por matriz
                Columnas disponibles:
                1 - Población total
                2 - Porcentaje analfabeta
                3 - Porcentaje sin educación básica
                4 - Porcentaje sin drenaje ni excusado
                5 - Porcentaje sin electricidad
                6 - Porcentaje sin agua
                7 - Porcentaje con piso de tierra
                8 - Porcentaje con hacinamiento
                9 - Porcentaje sin refrigerador
                10 - Índice de marginación
                11 - Índice de marginación normalizado
                > Ingresa dos listas de opciones de la forma '1,3,2 : 4,3': 1,2
                > Opción no válida
                > Ingresa dos listas de opciones de la forma '1,3,2 : 4,3': 1,2 : 3,a
                > Opción no válida
                > Ingresa dos listas de opciones de la forma '1,3,2 : 4,3': 1,2 : 3,5
                [['POB_TOT', 'ANALF'], ['SBASC', 'OVSEE']]
                ```
            * Pistas:
                * Hacer uso del método `self.mostrar_columnas_numericas()` para desplegar la lista.
                * Hacer uso del atributo `self.cols_numeracion` para recuperar el nombre de las columnas si tenemos la numeración correspondiente.
                * Considerar usar la función `.split` de los `str` para dividir textos de la entrada ingresada.
        
        * `menu_secundario_marginacion_territorio(self)`: este método debe mostrar el menú correspondiente a la funcionalidad de `Marginación por territorio` del menú principal.
            * Al inicio debe mostrar una pequeña fila de arteriscos seguido del texto `Marginación por territorio`.
            * La lista de opciones debe ser la que despliega el método `self.mostrar_estados`, es decir, las claves de los estados junto con sus nombres.
            * Al mismo tiempo debe solicitar que el usuario ingrese la clave de dos dígitos correspondiente a su elección.
            * Si la clave no es válida, es decir, no está registrada en `self.estados` y tampoco es la clave `00` entonces se debe mostrar el mensaje `> Opción no válida` y debe pedir las dos listas de nuevo sin mostrar el menú otra vez.
            * La clave ingresada se debe retornar en dos dígitos tal cual fue ingresada por el usuario como un `str`.
            * El funcionamiento del menú debe verse como el siguiente ejemplo, no se muestran todos los estados por cuestiones de espacio:
                ```bash
                ****************************************
                    Marginación por territorio       
                Estados disponibles:
                00 - Todos
                01 - Aguascalientes
                02 - Baja California
                03 - Baja California Sur
                04 - Campeche
                05 - Coahuila de Zaragoza
                06 - Colima
                ...
                32 - Zacatecas
                > Ingresa la clave de dos dígitos: a
                > Opción no válida
                > Ingresa la clave de dos dígitos: 33
                > Opción no válida
                > Ingresa la clave de dos dígitos: 06
                '06'
                ```
            * Pistas:
                * Hacer uso del método `self.mostrar_estados()` para desplegar la lista.
                * Hacer uso del atributo `self.estados` para validar la clave del estado.
        
        * `iniciar(self)`: este método debe ejecutar el ciclo principal de la aplicación.
            * Debe mostrar el menú principal solicitando una opción, dependiendo de la opción es el menú secundario que se va a mostrar y la funcionalidad que se va a ejecutar. A continuación se describe la funcinalidad que debe ejecutar cada opción:
                * Opción 1 (Graficas por pares): el objetivo es solicitar una lista de parejas numéricas para mostrar en una misma ventana las figuras correspondientes a cada pareja. Las pistas son las siguientes:
                    * Hacer uso del método `self.menu_secundario_graficas_pares` para mostrar la lista de columnas numéricas y solicitar una lista de parejas de columnas.
                    * Obtener todos los datos de la tabla `self.tabla_marginacion`, haciendo uso del método `select`.
                    * Usar la función `grafico_por_pares(datos, pares)` del módulo `graficador` la cual recibe el conjunto de datos tal cual es obtenido de la tabla y la lista de parejas de columnas obtenida en el primer paso. Dicha función generará las gráficas correspondientes.
                    * Nota: es posible que la generación de las gráficas sea muy lenta porque son muchos datos.
                * Opción 2 (Gráficas por matriz): el objetivo es solicitar dos lista de columnas numéricas, una lista para los ejes `x` y la otra para los ejes `y`, usar estas listas para mostrar en una misma ventana una matriz de gráficos uno para cada combinación de la lista del eje `x` contra la lista del eje `y`. Las pistas son las siguientes:
                    * Hacer uso del método `self.menu_secundario_graficas_matriz` para mostrar la lista de columnas numéricas y solicitar las dos listas de columnas, la primera para el eje `x` y la segunda para el eje `y`.
                    * Obtener todos los datos de la tabla `self.tabla_marginacion`, haciendo uso del método `select`.
                    * Usar la función `grafico_por_pares_producto(datos, cols_x, cols_y)` del módulo `graficador` la cual recibe el conjunto de datos tal cual es obtenido de la tabla y las listas de columnas obtenidas en el primer paso, enviar cada lista en un parámetro separado. Dicha función generará las gráficas correspondientes. 
                    * Nota: es posible que la generación de las gráficas sea muy lenta porque son muchos datos.
                    * Nota: solo en este caso no pude lograr que seaborn respetara el color ni el orden de los niveles de marginación.
                * Opción 3 (Gráficas por matriz): el objetivo es solicitar una clave de dos dígitos de estado o la clave `00` correspondiente a todos los estados y usar la clave obtenida para generar una gráfica de barras acumulada que muestre el porcentaje de cada grupo de marginación en cada región, si la clave es `00` entonces las regiones serán los estados pero si la clave es de un estado entonces las regiones serán los municipios.
                    * Hacer uso del método `self.menu_secundario_marginacion_territorio` para mostrar la lista de estados y solicitar la clave de dos dígitos deseada.
                    * Obtener datos de la tabla `self.tabla_marginacion` haciendo uso del método `select`, pero en este caso usar el parámetro `where` para obtener solamente los datos que correspondan a la clave de estado obtenida. Si la clave es `00`, entonces se deben obtener todos los datos de la tabla.
                    * Usar la función `grafico_barras_acumulado(datos)` del módulo `graficador` la cual solo recibe el conjunto de datos tal cual es obtenido de la tabla. Dicha función generará la gráfica correspondiente y resolverá automaticamente el tipo de regiones a usar.
                * Opción 4 (Salir del programa): salir del programa.
            * El ciclo debe repetirse mientras el usuario no ingrese la opción para salir del programa.


### Ejecutar la aplicación

Una vez implementado todo, para ejecutar la aplicación se debe de generar una instancia de la clase `App` e invocar el método `iniciar()`. Esto ya está implementado hasta abajo en el módulo `App.py` en la sección `if __name__ = '__main__'`, por lo que para ejecutar la aplicación se debe de colocar la terminal en la carpeta `src` y usar:
```bash
python .\app.py
```
Pero para que vayan probando lo que van implementando lo mejor es comentar la linea `app.iniciar()` para poner su código de pruebas, y regresarlo al estado orignal cuando estén listos.