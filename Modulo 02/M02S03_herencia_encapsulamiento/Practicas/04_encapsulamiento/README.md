Encapsulamiento
=================

En Python, el ***encapsulamiento*** se refiere al mecanismo de proteger los atributos de una clase, de modo que solo la clase pueda usarlos y que además pueda proveer métodos para manipularlos de manera segura (getters y setters).
* Esto se lleva a cabo mediante atributos privados o atributos protegidos.
* Este mecanismo no es del todo real en sí, si no más bien una convención entre la comunidad de Python.

Sintaxis:
----------
* Los atributos (métodos) privados se definen con un guión bajo precediendo el nombre del atributo. Por ejemplo `self._num_pedidos`.
    * Es importante remarcar que esto solo es una convención entre la comunidad de programadores de Python, ya que eso no impide el acceso y modificación de dichos atributos.
    * La idea es respetar esta convención y nunca consultar ni modificar atributos que comiencen con un `'_'`, aunque en realidad sí es posible hacerlo.
* Los atributos (métodos) protegidos se definen con dos guiones bajos precediendo el nombre del atributo. Por ejemplo `self.__num_pedidos`.
    * En este caso ya no es posible acceder ni modificar directamente el atributo con ese nombre.
    * La realidad es que Python cambia el nombre del atributo en todos los lugares donde aparece, pero solo dentro del cuerpo de la clase.
    * El atributo sigue existiendo, pero con un nombre un poco diferente.
    * Incluso sabiendo eso, es importante respetar el atributo y no acceder a este desde fuera de la clase usando su nombre alterado.
    * El objetivo de este mecanismo solo es proteger el atributo, para que sea muy poco probable que al heredar a una subclase, vaya a haber problemas si se define otro atributo con el mismo nombre en la subclase.
