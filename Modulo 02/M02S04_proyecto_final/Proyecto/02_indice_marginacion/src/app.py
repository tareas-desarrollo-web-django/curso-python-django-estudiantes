import pdb

import configuracion
from manejador_sqlite.tablas import TablaMarginacion
from importar_datos import importar_csv


class App:
    def __init__(self):
        # Atributos
        self.estados = None
        self.cols_numeracion = None
        self.tabla_marginacion = TablaMarginacion(configuracion.RUTA_BD)

        # Generamos los datos
        importar_csv(configuracion.RUTA_CSV_MARGINACION, self.tabla_marginacion)
        self._generar_estados()
        self._generar_numeracion_columnas()

    def _generar_estados(self):
        r"""
        Al ejecutar este método la tabla en `self.tabla_marginacion` debió 
        importar los datos de marginación. Este método genera el contenido del 
        atributo `self.estados` que es una diccionario con los distintos 
        estados que aparecen en la tabla de marginación. El diccionario mapea 
        la clave del estado como está dada en la columna 'ENT' de la tabla al
        nombre del estado como está en la columna `NOM_ENT`. Los datos no son 
        retornados sino que son asignados al atributo `self.estados`. 
        Los datos son los siguientes:
        `{'01': 'Aguascalientes', '02': 'Baja California', ...}`
        """
        self.estados = dict(self.tabla_marginacion.select_distinct(['ENT', 'NOM_ENT']))

    # PROYECTO
    def _generar_numeracion_columnas(self):
        r"""
        Usar la tabla `TablaMarginacion` para generar un diccionario que asigna 
        a cada una de sus columnas columna un índice comenzando desde uno.
        El diccionario debe mapear el índice asignado a una tupla que contenga
        el nombre de la columna y el descriptivo, tal cual están registrados
        en la tabla `TablaMarginacion`, pero solo deben estar las columnas 
        que estén registradas de tipo REAL o INTEGER. Hay que revisar el código
        de la clase `TablaMarginacion` para decidir como implementar eso.
        El diccionario generado debe ser como el siguiente ejemplo, pero no
        debe ser retornado sino que debe ser asignado al atributo 
        `self.cols_numeracion`:
        {
            1: ('POB_TOT', 'Población total'),
            2: ('ANALF', 'Porcentaje analfabeta'),
            3: ('SBASC', 'Porcentaje sin educación básica'),
            ...
            11: ('IMN_2020', 'Índice de marginación normalizado')
        }

        PISTAS:
        - El orden de la numeración no importa, solo que unicamente estén
        las columnas REAL o INTEGER.
        - Hacer uso del atributo `TablaMarginacion.columnas`.
        - Para saber si una columna es REAL solo debemos revisar si 'real'
        está en la versión en minúsculas de la propiedad 'attributes' de la 
        columna y similar para saber si es INTEGER.
        """
        print(f"Se debe implementar el método '{self.__class__.__name__}._generar_numeracion_columnas()'")

    # PROYECTO
    def menu_principal(self):
        r"""
        Este método debe mostrar en la terminal un menú y al mismo tiempo debe 
        solicitar al usuario que ingrese una opción. Si la opción ingresada no 
        es válida se debe mostrar el mensaje '> Opción no válida' y debe pedir 
        la opción de nuevo sin mostrar el menú otra vez, como en el siguiente
        ejemplo. Mostrar una pequeña fila de arteriscos al inicio. La opción 
        ingresada final se debe retornar como un entero:
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
        Pistas:
        - Al convertir a entero con `int` si el valor no es convertible 
        se arroja una excepción de tipo `ValueError`, podemos complementar
        arrojando nosotros un `raise ValueError()` si la opción sí es entera
        pero no está en el rango del menú. Podríamos aprovechar esto con un 
        bloque `try ... except`.
        """
        print(f"Se debe implementar el método '{self.__class__.__name__}.menu_principal()'")
        
        return 4

    # PROYECTO
    def mostrar_columnas_numericas(self):
        r"""
        Este método debe mostrar una lista estilo menú con los descriptivos de 
        las columnas almacenadas en el atributo `self.cols_numeracion` que fue 
        generado con el método `self._generar_numeracion_columnas`. El orden 
        de la numeración debe ser idéntica a como está definida en el atributo
        `self.cols_numeracion`, en este caso no debe solicitar ninguna opción,
        ya que este método será usado por otros métodos que sí solicitan 
        entrada en base a esta lista. La lista debe verse como el siguiente
        ejemplo:
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
        """
        print(f"Se debe implementar el método '{self.__class__.__name__}.mostrar_columnas_numericas()'")

    # PROYECTO
    def mostrar_estados(self):
        r"""
        Este método debe mostrar una lista estilo menú con los estados 
        almacenados en el atributo `self.estados`, además, al inicio de la 
        lista debe estar la opción `00 - Todos`, usamos la clave `00` porque
        esa no corresponde a ningún estado. No debe solicitar ninguna opción,
        ya que este método será usado por otros métodos que sí solicitan 
        entrada en base a esta lista.
        La lista debe verse como el 
        siguiente ejemplo:
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
        """
        print(f"Se debe implementar el método '{self.__class__.__name__}.mostrar_estados()'")

    # PROYECTO
    def menu_secundario_graficas_pares(self):
        r"""
        Este método debe mostrar el menú correspondiente a la funcionalidad de 
        `Gráficas por pares` del menú principal. 
        * Al inicio debe mostrar una pequeña fila de arteriscos seguido del
        texto `Gráficas por pares`.
        * La lista de opciones debe ser la que despliega el método 
        `self.mostrar_columnas_numericas`, es decir, la numeración de las 
        columnas numéricas junto con los descriptivos. 
        * Al mismo tiempo debe solicitar que el usuario ingrese parejas de 
        columnas mediante los números asignados a cada columna en la lista. 
        Las parejas deben ser ingresadas en la forma `1:3, 2:4, 3:5`,
        los espacios no deben importar.
        * Si la lista ingresada no es válida, ya sea porque un valor no es 
        entero o está fuera del rango de la lista entonces se debe mostrar el 
        mensaje '> Opción no válida' y debe pedir las parejas de nuevo sin 
        mostrar el menú otra vez.
        * Las parejas ingresadas se deben retornar pero como nombres de columnas
        de la tabla de marginación en correspondencia con el menú, es decir, 
        si el usuario ingresa '1:3, 2:4' se debe retornar 
        `[('POB_TOT', 'SBASC'), ('ANALF', 'OVSDE')]`, porque esos son los 
        nombres de las columnas que corresponden a la numeración.
        * El funcionamiento del menú debe verse como el siguiente ejemplo:
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
        
        Pistas:
        - Hacer uso del método `self.mostrar_columnas_numericas()` para 
        desplegar la lista.
        - Hacer uso del atributo `self.cols_numeracion` para recuperar el
        nombre de las columnas si tenemos la numeración correspondiente.
        - Considerar usar la función `.split` de los `str` para dividir textos
        de la entrada ingresada.
        """
        print(f"Se debe implementar el método '{self.__class__.__name__}.menu_secundario_graficas_pares()'")

        return []

    # PROYECTO
    def menu_secundario_graficas_matriz(self):
        r"""
        Este método debe mostrar el menú correspondiente a la funcionalidad de 
        `Gráficas por matriz` del menú principal. 
        * Al inicio debe mostrar una pequeña fila de arteriscos seguido del
        texto `Gráficas por matriz`.
        * La lista de opciones debe ser la que despliega el método 
        `self.mostrar_columnas_numericas`, es decir, la numeración de las 
        columnas numéricas junto con los descriptivos. 
        * Al mismo tiempo debe solicitar que el usuario ingrese dos listas de 
        números de opciones del menú. Las listas deben deben ser ingresadas en 
        la forma `1,3,2 : 4,3`, que representaría a las listas `[1, 3, 2]` y 
        `[4, 3]`, los espacios no deben importar.
        * Si las listas ingresadas no son válidas, ya sea porque un valor no es 
        entero, está fuera del rango del menú o no se dieron 2 listas entonces 
        se debe mostrar el mensaje `> Opción no válida` y debe pedir las dos 
        listas de nuevo sin mostrar el menú otra vez.
        * Las listas ingresadas se deben retornar pero como nombres de columnas
        de la tabla de marginación en correspondencia con el menú, es decir, 
        si el usuario ingresa `1,2 : 3, 5, 6` se debe retornar 
        `[['POB_TOT', 'ANALF'], ['SBASC', 'OVSEE', 'OVSAE']]`, porque esos son 
        los nombres de las columnas que corresponden a la numeración.
        * El funcionamiento del menú debe verse como el siguiente ejemplo:
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

        
        Pistas:
        - Hacer uso del método `self.mostrar_columnas_numericas()` para 
        desplegar la lista.
        - Hacer uso del atributo `self.cols_numeracion` para recuperar el
        nombre de las columnas si tenemos la numeración correspondiente.
        - Considerar usar la función `.split` de los `str` para dividir textos
        de la entrada ingresada.
        """
        print(f"Se debe implementar el método '{self.__class__.__name__}.menu_secundario_graficas_matriz()'")

        return []

    # PROYECTO
    def menu_secundario_marginacion_territorio(self):
        r"""
        Este método debe mostrar el menú correspondiente a la funcionalidad de 
        `Marginación por territorio` del menú principal. 
        * Al inicio debe mostrar una pequeña fila de arteriscos seguido del
        texto `Marginación por territorio`.
        * La lista de opciones debe ser la que despliega el método 
        `self.mostrar_estados`, es decir, las claves de los estados junto
        con sus nombres.
        * Al mismo tiempo debe solicitar que el usuario ingrese la clave de dos
        dígitos correspondiente a su elección.
        * Si la clave no es válida, es decir, no está registrada en 
        `self.estados` y tampoco es la clave `00` entonces se debe mostrar el 
        mensaje `> Opción no válida` y debe pedir las dos listas de nuevo sin 
        mostrar el menú otra vez.
        * La clave ingresada se debe retornar en dos dígitos tal cual fue 
        ingresada por el usuario como un `str`.        
        * El funcionamiento del menú debe verse como el siguiente ejemplo, no
        se muestran todos los estados por cuestiones de espacio:
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
        
        Pistas:
        - Hacer uso del método `self.mostrar_estados()` para desplegar la lista.
        - Hacer uso del atributo `self.estados` para validar la clave del 
        estado.
        """
        print(f"Se debe implementar el método '{self.__class__.__name__}.menu_secundario_marginacion_territorio()'")

        return ""

    # PROYECTO
    def iniciar(self):
        r"""
        Este método debe ejecutar el ciclo principal de la aplicación.
        * Debe mostrar el menú principal solicitando una opción, dependiendo
        de la opción es el menú secundario que se va a mostrar y la 
        funcionalidad que se va a ejecutar. A continuación se describe la
        funcinalidad que debe ejecutar cada opción:
        * Opción 1 (Graficas por pares): el objetivo es solicitar una lista de 
        parejas numéricas para mostrar en una misma ventana las figuras 
        correspondientes a cada pareja. Las pistas son las siguientes:
            * Hacer uso del método `self.menu_secundario_graficas_pares` para
            mostrar la lista de columnas numéricas y solicitar una lista de
            parejas de columnas.
            * Obtener todos los datos de la tabla `self.tabla_marginacion`, 
            haciendo uso del método `select`.
            * Usar la función `grafico_por_pares(datos, pares)` del módulo 
            `graficador` la cual recibe el conjunto de datos tal cual es 
            obtenido de la tabla y la lista de parejas de columnas obtenida en
            el primer paso. Dicha función generará las gráficas 
            correspondientes.
            * Nota: es posible que la generación de las gráficas sea muy lenta
            porque son muchos datos.
        * Opción 2 (Gráficas por matriz): el objetivo es solicitar dos lista de 
        columnas numéricas, una lista para los ejes `x` y la otra para los ejes
        `y`, usar estas listas para mostrar en una misma ventana una matriz de 
        gráficos uno para cada combinación de la lista del eje `x` contra la 
        lista del eje `y`. Las pistas son las siguientes:
            * Hacer uso del método `self.menu_secundario_graficas_matriz` para
            mostrar la lista de columnas numéricas y solicitar las dos listas de
            columnas, la primera para el eje `x` y la segunda para el eje `y`.
            * Obtener todos los datos de la tabla `self.tabla_marginacion`, 
            haciendo uso del método `select`.
            * Usar la función `grafico_por_pares_producto(datos, cols_x, cols_y)` 
            del módulo `graficador` la cual recibe el conjunto de datos tal 
            cual es obtenido de la tabla y las listas de columnas obtenidas en
            el primer paso, enviar cada lista en un parámetro separado. Dicha 
            función generará las gráficas correspondientes. 
            * Nota: es posible que la generación de las gráficas sea muy lenta
            porque son muchos datos.
        * Opción 3 (Gráficas por matriz): el objetivo es solicitar una clave
        de dos dígitos de estado o la clave `00` correspondiente a todos los
        estados y usar la clave obtenida para generar una gráfica de barras
        acumulada que muestre el porcentaje de cada grupo de marginación en 
        cada región, si la clave es `00` entonces las regiones serán los estados
        pero si la clave es de un estado entonces las regiones serán los 
        municipios.
            * Hacer uso del método `self.menu_secundario_marginacion_territorio` 
            para mostrar la lista de estados y solicitar la clave de dos dígitos
            deseada.
            * Obtener datos de la tabla `self.tabla_marginacion` haciendo uso 
            del método `select`, pero en este caso usar el parámetro `where` 
            para obtener solamente los datos que correspondan a la clave de 
            estado obtenida. Si la clave es `00`, entonces se deben obtener 
            todos los datos de la tabla.
            * Usar la función `grafico_barras_acumulado(datos)` del módulo 
            `graficador` la cual solo recibe el conjunto de datos tal 
            cual es obtenido de la tabla. Dicha función generará la gráfica
            correspondiente y resolverá automaticamente el tipo de regiones a 
            usar.
        * Opción 4 (Salir del programa): salir del programa.
        * El ciclo debe repetirse mientras el usuario no ingrese la opción
        para salir del programa.
        """
        print(f"Se debe implementar el método '{self.__class__.__name__}.iniciar()'")


if __name__ == '__main__':
    app = App()
    app.iniciar()








