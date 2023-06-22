Excepciones predefinidas
=========================

Para estandarizar el manejo de errores, Python tiene un conjunto de Excepciones predefinidas:
* En lugar de crear nuestras propias excepciones, lo mejor es usar las que vienen predefinidas.
* Siempre es bueno revisar la lista oficial, para usar las que mejor expliquen el tipo de error que queremos informar.
* La lista es muy grande y se puede consultar en https://docs.python.org/es/3/library/exceptions.html.
* Algunas de las excepciones más comunes son:
    * `IndexError`: se arroja cuando un indice de una secuencia está fuera de rango.
    * `KeyError`: se arroja cuando la llave de un mapeador (ej. diccionario) no existe.
    * `NotImplementedError`: se arroja cuando un método no está implementado, es usado comunmente en herencia.
    * `TypeError`: se arroja cuando una función recibe un parámetro de tipo incorrecto.
    * `ValueError`: se arroja cuando una función recibe un parámetro de tipo correcto, pero el valor no es válido.
    * `ZeroDivisionError`: se arroja cuando va a ocurrir una división por cero.


Sintaxis:
----------
* Cuando en un bloque de código hemos detectado un error que no corresponde manejar a dicho bloque, lo mejor es arrojar una excepción. Esto se hace con la sitaxis:
  ```python
  raise Excepcion(*args)
  ```
* Para capturar y manejar los errores arrojados se usan bloques `try-except`:
  ```python
  try:
    tabla = cargar_tabla('datos.csv')
  except TypeError:
    # Código para manejar la excepción TypeError
    ...
  except ValueError as err: # Atrapamos la excepción en la variable 'err'
    # Código para manejar la excepción ValueError
    ...
  except:
    # Código por defecto para manejar cualquier excepción del tipo que sea.
    # Se recomienda tener mucho cuidado al usar esta cláusula, 
    # de preferencia no usarla.
    ...
  ```
* El flujo de manejo de las excepciones es el siguiente:
  * El código que queremos monitoriear por errores debe estar encerrado en un bloque `try`.
  * Si se ocurre ningún error, los bloques `except` serán ignorados.
  * Si ocurre un error, se revisará si más adelante en el flujo del programa hay una `except` que captura dicha excepción.
    * Si se encuentra entonces se ejecutará el bloque y el programa continuará su flujo normal a partir de ahí.
    * Si no se encuentra ninguno entonces el programa terminará con un mensaje de error en la salida estándar.
