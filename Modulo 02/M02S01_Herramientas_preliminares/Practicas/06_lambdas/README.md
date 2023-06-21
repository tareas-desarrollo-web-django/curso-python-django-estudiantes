Expresiones lambda
===================

Las expresiones lambda, también conocidas como funciones anónimas, tienen el único propósito de evaluar una expresión:
* Son invocables y pueden recibir parámetros
* Son muy útiles como funciones auxiliares
* Suelen usarse como parámetros para otras funciones que transforman datos

Sintaxis:
----------

* La sintaxis básica de una expresión lambda es: `lambda *args: expresion`
* Un ejemplo más concreto: `lamdda a, n: a ** n`
* Los parámetros también soportan valores por defecto: `lamdda a, n=2: a ** n`