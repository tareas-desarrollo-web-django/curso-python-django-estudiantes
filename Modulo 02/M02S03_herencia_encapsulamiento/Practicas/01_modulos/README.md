Módulos
=========

En Python, un módulo es simplemente un script `.py`:
* El nombre del archivo será el nombre del módulo, por ejemplo si el script se llama `mi_modulo.py`, entonces el nombre del módulo será `mi_modulo`.
* Todos lo que esté dentro del módulo formará parte de los componentes del módulo.
* Para importar un módulo solo hacemos uso de `import`: por ejemplo, `import mi_modulo`.
    * Todos los componentes del módulo (funciones, clases, variables, etc) serán accesibles a través del espacio de nombres `mi_modulo`, por ejemplo: `mi_modulo.mi_funcion()`.
* Podemos importar componentes en particular de un módulo con `from`.
    * Por ejemplo: `from mi_modulo import mi_funcion`
    * De esa forma ya podemos usar `mi_funcion` directamente sin usar como prefijo el módulo.

