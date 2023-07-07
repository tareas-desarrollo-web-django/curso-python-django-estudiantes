Gráficas de funciones
=======================

Clase PuntoCartesiano
-----------------------

Esta clase se encuentra definida en el módulo `punto_cartesiano` e implementa 
el comportamiento de un punto cartesiano $(x,y)$.

Para el proyecto final, lo único que hay que saber es que para construir un 
objeto de este tipo, solo tenemos que pasar al constructur la coordenada $x$ 
y la coordenada $y$. Ejemplo: `p = PuntoCartesiano(1, 8.5)`.

Si se quiere saber más acerca de lo que implementa la clase `PuntoCartesiano`,
se puede revisar el código, casi todo ya lo habíamos visto en clase.

Clase PlanoCartesiano
-----------------------

Esta clase se encuentra definida en el módulo `plano_cartesiano` e implementa
el funcionamiento de manera gráfica de un plano cartesiano para visualizar
y puntos, circulos y rectas usando coordenadas cartesianas, tal cual como si
estuviéramos en un plano cartesiano.

Como cualquier gráfica de un plano cartesiano, para que funcione, debemos 
definir cual es el área que será visible de dicho plano, también conocida como
dominio. En esta implementación, el área visible del plano está separada en 
dos atributos.
* El atributo `self.x_dominio` es una tupla que contiene el rango visible
del eje $x$, es decir, los valores `(x_min, x_max)` del rango visible del eje
$x$.
* El atributo `self.y_dominio` es una tupla que contiene el rango visible
del eje $y$, es decir, los valores `(y_min, y_max)` del rango visible del eje
$y$.

Para el proyecto, lo único que hay que saber es el funcionamiento del atributo
`self.x_dominio`, el cual acabamos de describir en los puntos anteriores. 
Y también saber que la función:
* `self.linea_cart(p, q, color, ancho=1)`: dibuja una linea en el plano
desde el punto cartesiano `p` hasta el punto cartesiano `q`, del color y ancho
especificados.

Si se quiere saber más acerca de lo que implementa la clase `PlanoCartesiano`,
se puede revisar la documentación que hay dentro de cada método de dicha clase.
Aunque no es necesario para este proyecto, las funciones más importantes son:
* `self.ajustar_dominio(x_dominio, y_dominio)`: cambia el area visual del plano
cartesiano.
* `self.ajustar_dominio_proporcional(x_dominio, y_dominio, encuadre)`: cambia 
el area visual del plano cartesiano, pero sin causar distorsión.
* `self.circulo_cart(centro, radio, color, ancho=0)`: dibuja un circulo en el 
plano cartesiano en el centro, radio y color especificados. Si el ancho es 
cero, entonces el circulo será de color relleno, si es mayor que
cero entonces solo se dibujará el borde del círculo.
* `self.punto(p, color, tamano=3)`: dibuja un punto circular del color y 
tamaño especificados. El tamaño es es pixels.

Clase GraficaFuncion
-----------------------

Esta clase hereda todo el funcionamiento de la clase PlanoCartesiano, tanto
atirbutos como métodos. Está implementada en el script `exercise.py`. El
proyecto consiste en implementar dos métodos de esta clase para que el 
sistema graficador de funciones esté completo y funcional.

En el constructor de la clase `GraficaFuncion` no hay nada que hacer, solo
mencionar que recibe dos parámetros:
* El primer parámetro es una función que recibe un valor y devuelve otro valor.
Esta función puede ser una expresión lambda, por ejemplo: 
`lambda x: x * x`. Esta función se almacena en el atributo `self._f`.
* El otro parámetro es opcional y representa cada cuanto vamos a evaluar la
función para generar su gráfica. Este parámetro se almacena en el parámetro
`self.dx`.

### Actividades

Los métodos a implementar en la clase `GraficaFuncion` son los siguientes:
* `self._construir_grafica()`: debe generar una lista de objetos `PuntoCartesiano`.
La lista no se debe retornar, sino que debe quedar almacenada en el atributo
`self._grafica`.
    * Cada punto cartesiano $(x, y)$ agregado a la lista corresponde a un punto
    en la gráfica de la función recibida en el constructor. Es decir, $x$ es 
    un valor en el dominio del eje x, y el valor de $y$ sería el resultado 
    de evaluar la función `self._f` en dicho valor de $x$.
    * Recuerden que el dominio del eje x está definido en el atributo 
    `self.x_dominio`.
    * La idea es agregar a la lista los puntos cartesianos $(x, f(x))$, 
    donde `x` empieza en `self.x_dominio[0]` y llega hasta `self.x_dominio[1]`, con
    separaciones de tamaño `self.dx`.
    * Recuerden inicializar la lista `self._grafica` a una lista vacía antes de
    empezar a agregar puntos.
* `self.dibujar_escena()`: aquí es donde dibujaremos la lineas que conecten los
puntos que generamos en `self._grafica` mediante el método anterior.
    * Lo primero que hay que hacer en este método es invocar al método 
    `self._construir_grafica()`.
    * Luego hay que dibujar una linea entre cada pareja de puntos consecutivos
    de la lista `self._grafica`, usando el método `self.linea_cart(...)` el cual
    describimos anteriormente. Es decir, dibujamos una linea entre el primer 
    punto de la lista y el segundo, luego una linea entre el segundo y 
    el tercero, luego una entre el tercero y el cuarto, y así hasta llegar 
    al último punto de la lista.

Y eso es todo, una vez implementados esos dos métodos, deberían tener un 
graficador de funciones completamente funcional que se puede arrastrar con el
mouse y hacer zoom con la llantita del mouse. Al hacer zoom manteniendo
presionado `CTRL`, solo se afecta el eje y, pero manteniendo presionado `ALT` solo
se afecta el eje x.

Para ejecutar el programa solo tienen que ejecutar el script `exercise.py`, 
como hacemos usualmente en clases.