Matriz transpuesta
================================================

La transpuesta de una matriz es una matriz resultante de convertir las filas en columnas y las columnas en filas, respetanto el acomodo de estas. Es decir, la primera columna se convierte en la primera fila, etc.

Por ejemplo:

$$\begin{pmatrix}
1 & 3 \\
5 & 2
\end{pmatrix}^T=
\begin{pmatrix}
1 & 5 \\
3 & 2
\end{pmatrix}$$

Problema
--------

En el archivo `src\exercise.py` implementar una clase llamada `Matriz`:

* El constructor de la clase debe recibir como parámetro una matriz, para almacenarla como atributo.
    * No hay restricciones en el tamaño de la matriz.
    * La matriz debe ser dada en una tupla de tuplas, cada tupla interna es una fila de la matriz.
    * Excepciones del constructor (indicar un mensaje de error):
        * `ValueError`: si la matriz no es pareja, es decir, que el tamaño de sus filas no sea igual para todas.
* La clase debe contener un método con firma `transpuesta(self)`.
    * Debe retornar la transpuesta de la matriz dada en el constructor, también como una tupla de tuplas.


