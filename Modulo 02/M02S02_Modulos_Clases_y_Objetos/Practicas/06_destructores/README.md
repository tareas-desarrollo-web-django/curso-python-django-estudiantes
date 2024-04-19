Destructores de clase
=======================

El ***destructor*** es una método especial que se ejecuta cuando la memoria de un objeto es recolecada por el recolector de basura, lo cual ocurre cuando la última referencia al objeto es eliminada.
* De acuerdo a la [documentación](https://docs.python.org/3/reference/datamodel.html), el recolector de basura tiene el objetivo de recolectar objetos tan pronto como dejen de tener referencias.
* Generalmente se usa para liberar los recursos usados por el objeto, aunque podemos usarlo como nos convenga.

Sintaxis:
----------

* El destructor es un método que debe estar definido dentro de una clase y cuya firma es `def __del__(self):`.

