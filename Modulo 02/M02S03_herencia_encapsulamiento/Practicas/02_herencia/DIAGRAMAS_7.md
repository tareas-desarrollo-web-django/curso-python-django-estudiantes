Composición sobre herencias
============================

El mecanismo de composición es cuando una clase **A** se integra a otra a través de un atributo el cual es definido como un objeto de tipo **A**.
* De esta forma quedan dos clases completamente disjuntas las cuales podemos modificar de manera prácticamente independiente una de la otra.
* Lo mejor darle prioridad a la composición antes que a la herencia.

Herencia
---------
```mermaid
classDiagram
    class Empleado{
        ...
    }
    class Domicilio{
        ...
    }
    class Salarios{
        ...
    }
    class Actividades{
        ...
    }
    Domicilio <|-- Empleado
    Salarios <|-- Empleado
    Actividades <|-- Empleado
```

Composición
---------
```mermaid
classDiagram
    class Empleado{
        domicilio: Domicilio
        salarios: Salarios
        actividades: Actividades
        ....()
    }
    class Domicilio{
        ...
    }
    class Salarios{
        ...
    }
    class Actividades{
        ...
    }
    Empleado *-- Domicilio
    Empleado *-- Salarios
    Empleado *-- Actividades
```
