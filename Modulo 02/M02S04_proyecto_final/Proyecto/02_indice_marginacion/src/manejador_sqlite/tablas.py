from .tablas_sqlite import TablaSQLite

class TablaMarginacion(TablaSQLite):
    r"""
    Tabla para almacenar los datos de INEGI del indice de marginacion

    NOTE: a cada columna le agregamos una propiedad 'descriptivo', que no se usa
    en `TablaSQLite`, pero que la usaremos nosotros para mostrar nombres 
    descriptivos de las columnas en gráficos, menús, etc.
    """
    nombre_tabla = 'marginacion'
    columnas = {
        # Clave geográfica
        'CVE_LOC': {
            'attributes': 'TEXT PRIMARY KEY',
            'descriptivo': 'Clave geográfica'
        },
        # Clave de la entidad federativa
        'ENT': {
            'attributes': 'TEXT',
            'descriptivo': 'Clave de estado'
        },
        # Nombre de la entidad federativa
        'NOM_ENT': {
            'attributes': 'TEXT',
            'descriptivo': 'Estado'
        },
        # Clave del municipio
        'MUN': {
            'attributes': 'TEXT',
            'descriptivo': 'Clave de municipio'
        },
        # Nombre del municipio
        'NOM_MUN': {
            'attributes': 'TEXT',
            'descriptivo': 'Municipio'
        },
        # Clave de la localidad
        'LOC': {
            'attributes': 'TEXT',
            'descriptivo': 'Clave de localidad'
        },
        # Nombre de la localidad
        'NOM_LOC': {
            'attributes': 'TEXT',
            'descriptivo': 'Localidad'
        },
        # Población total
        'POB_TOT': {
            'attributes': 'INTEGER',
            'descriptivo': 'Población total'
        },
        # Porcentaje de población de 15 años o más analfabeta
        'ANALF': {
            'attributes': 'REAL',
            'descriptivo': 'Porcentaje analfabeta'
        },
        # Porcentaje de población de 15 años o más sin educación básica
        'SBASC': {
            'attributes': 'REAL',
            'descriptivo': 'Porcentaje sin educación básica'
        },
        # Porcentaje de ocupantes en viviendas particulares habitadas sin drenaje ni excusado
        'OVSDE': {
            'attributes': 'REAL',
            'descriptivo': 'Porcentaje sin drenaje ni excusado'
        },
        # Porcentaje de ocupantes en viviendas particulares habitadas sin energía eléctrica
        'OVSEE': {
            'attributes': 'REAL',
            'descriptivo': 'Porcentaje sin electricidad'
        },
        # Porcentaje de ocupantes en viviendas particulares habitadas sin agua entubada
        'OVSAE': {
            'attributes': 'REAL',
            'descriptivo': 'Porcentaje sin agua'
        },
        # Porcentaje de ocupantes en viviendas particulares habitadas con piso de tierra
        'OVPT': {
            'attributes': 'REAL',
            'descriptivo': 'Porcentaje con piso de tierra'
        },
        # Porcentaje de ocupantes en viviendas particulares habitadas con hacinamiento
        'OVHAC': {
            'attributes': 'REAL',
            'descriptivo': 'Porcentaje con hacinamiento'
        },
        # Porcentaje de ocupantes en viviendas particulares habitadas sin refrigerador
        'OVSREF': {
            'attributes': 'REAL',
            'descriptivo': 'Porcentaje sin refrigerador'
        },
        # Índice de marginación a nivel localidad, 2020
        'IM_2020': {
            'attributes': 'REAL',
            'descriptivo': 'Índice de marginación'
        },
        # Grado de marginación a nivel localidad, 2020
        'GM_2020': {
            'attributes': 'TEXT',
            'descriptivo': 'Grupo de marginación'
        },
        # Índice de marginación normalizado a nivel localidad, 2020
        'IMN_2020': {
            'attributes': 'REAL',
            'descriptivo': 'Índice de marginación normalizado'
        },
    }
