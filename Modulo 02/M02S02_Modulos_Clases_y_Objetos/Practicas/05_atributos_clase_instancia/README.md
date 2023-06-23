Atributos de clase y atributos de instancia
================================================

Los atributos de instancia son aquellos que pertenecen a cada instancia en particular.
* Estos van declarados dentro del constructor.
* Solo pueden ser consultados por la instancia misma.

Los atributos de clase son aquellos que pertenecen a la clase.
* Estos van declarados fuera del constructor.
* Solo se pueden modificar desde la clase misma.
* Si se intenta modificar un atributo de clase desde una instancia, entonces se creará un atributo de instancia solo para la instancia en cuestión.
* Pueden ser consultados por la clase misma y por las instancias, siempre que la instancia no tengan ya un atributo con el mismo nombre.
    * Al consultar un atributo desde una instancia primero se revisa la instancia, si no hay un atributo con ese nombre en la instancia entonces se busca en la clase.
