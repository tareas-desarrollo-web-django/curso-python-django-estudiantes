import seaborn as sns
import seaborn.objects as so
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import math
import pdb

from manejador_sqlite.tablas import TablaMarginacion

# Tema por defecto de Seaborn
sns.set_theme()
# Para que pyplot no dibuje fuera del marco
matplotlib.rcParams.update({'figure.autolayout': True})

# Variable global para el orden en el que se deben manejar los grupos de marginación
orden_marginacion = ['Muy bajo', 'Bajo', 'Medio', 'Alto', 'Muy alto']
# Paleta para grupos de marginación, en el mismo orden que orden_marginacion
paleta_marginacion = sns.color_palette(['#4c78a8', '#54a24b', '#72b7b2', '#f58518', '#e45656'])

def grafico_por_pares(datos:list[dict], pares:list[tuple]):
    r"""
    Recibe una lista de `datos` que corresponden a filas de la tabla de 
    marginación, cada fila en un diccionario:
    [{'CVE_LOC': '010010001', 'ENT': '01', 'NOM_ENT': 'Aguascalientes', ...},
    {'CVE_LOC': '010010001', 'ENT': '01', 'NOM_ENT': 'Aguascalientes', ...}, 
    ...]
    También recibe una lista de `pares` de nombres de columnas de la tabla de
    marginación, cada pareja en una tupla:
    [('POB_TOT', 'ANALF'), ('POB_TOT', 'SBASC')]
    Dibuja una matriz de gráficos de puntos, donde cada gráfico corresponde 
    a una pareja de columnas de la lista dada.

    NOTE: mediante `sns.scatterplot` sí pude especificar el orden de los grupos
    y el color de cada grupo, a diferencia de `so.Plot`.
    """
    if not pares:
        raise ValueError(f'No se permite una lista vacía de pares: {pares}')
    
    datos = pd.DataFrame(datos)
    # datos = datos.sample(10000)

    # fig no lo usaremos, pero axes contiene una matriz de manejadores de subgráfico en la figura,
    # La idea es que los gráficos queden acomodados en una matriz cuadrada, el caso especial es cuando
    # tenemos 2 o menos elementos, en ese caso solo queremos una fila. A la hora de dibujar un gráfico
    # tenemos que indicar en que subfigura lo queremos dibujar.
    p = len(pares)
    k = math.ceil(math.sqrt(p)) 
    fig, axes = plt.subplots(k if p > 2 else 1, k, figsize=(12, 8))
    # El problema es que si la matriz es de 1xN, entonces solo se generará una fila no una matriz, y
    # si es de 1x1 entonces solo se generará un elemento individual, por lo que hacemos que siempre termine
    # en una matriz para mantener la generalidad.
    if p <= 2:
        axes = [[axes]] if p == 1 else [axes]
    
    # Dibujamos cada par en su subgráfico, coloreado por el grupo de marginación 'GM_2020'
    for i, (x_col, y_col) in enumerate(pares):
        ax = sns.scatterplot(
            datos, x=x_col, y=y_col, hue="GM_2020", hue_order=orden_marginacion, 
            palette=paleta_marginacion, ax=axes[i//k][i%k]
        )
        ax.set(
            xlabel=TablaMarginacion.columnas[x_col]['descriptivo'], 
            ylabel=TablaMarginacion.columnas[y_col]['descriptivo']
        )
    
    plt.tight_layout()
    plt.show()

def grafico_por_pares_producto(datos:list[dict], columnas_x:list[str], columnas_y:list[str]):
    r"""
    Recibe una lista de `datos` que corresponden a filas de la tabla de 
    marginación, cada fila en un diccionario:
    [{'CVE_LOC': '010010001', 'ENT': '01', 'NOM_ENT': 'Aguascalientes', ...},
    {'CVE_LOC': '010010001', 'ENT': '01', 'NOM_ENT': 'Aguascalientes', ...}, 
    ...]
    También recibe dos listas de nombres de columnas de la tabla de marginación,
    `columnas_x` y `columnas_y`, genera una matriz de gráficos de puntos, donde
    cada gráfico corresponde a una columna de cada lista, se generan todas las
    posibilidades.

    NOTE: creo que podríamos generalizar esta función para que también haga
    lo que hace la función `grafico_por_pares`, usando `cross=False`. El prblema
    es que con este método no logré especificar el orden de los grupos y el 
    color.
    TODO: Resolver el como especificar el orden de los grupos y el color.
    """
    if not columnas_x or not columnas_y:
        raise ValueError(f"No se permiten listas de columnas vacías: '{columnas_x=}', '{columnas_y=}'")
    
    datos = pd.DataFrame(datos)
    # datos = datos.sample(10000)

    # Retorna el descriptivo dado el nombre de la columna
    descriptivo = lambda c: TablaMarginacion.columnas[c]['descriptivo']

    (
        so.Plot(datos, color="GM_2020")
        .pair(x=columnas_x, y=columnas_y, cross=True)
        .label(x=descriptivo, y=descriptivo)
        .add(so.Dots(fillalpha=0.7))
    ).show()

def grafico_barras_acumulado(datos:list[dict]):
    r"""
    Recibe una lista de `datos` que corresponden a filas de la tabla de 
    marginación, cada fila en un diccionario:
    [{'CVE_LOC': '010010001', 'ENT': '01', 'NOM_ENT': 'Aguascalientes', ...},
    {'CVE_LOC': '010010001', 'ENT': '01', 'NOM_ENT': 'Aguascalientes', ...}, 
    ...]
    Genera una gráfica de barras acumulada (Stacked-Bar Chart) con los distintos
    grupos de marginación al nivel de la región correspondiente a los dados.
    Si los datos contienen información de un solo estado entonces las regiones
    serán los municipios pero si hay información de más de un estado entonces
    serán los estados.
    """
    datos = pd.DataFrame(datos)
    # datos = datos.sample(10000)

    if len(datos['ENT'].unique()) == 1:
        col_regiones = 'NOM_MUN'
    else:
        col_regiones = 'NOM_ENT'
    
    # Implementaré el Stacked-Bar via procesamiento de datos porque no encontré una forma de hacerlo con Seaborn.
    # Los pasos son: Generar por la cantidad de localidades en cada Sector-GrupoMarginacion
    datos = datos.groupby([col_regiones, 'GM_2020'])['GM_2020'].agg('count')
    # Generar una columna para cada grupo con la cantidad en el mismo orden que 'orden_marginacion'
    datos = datos.unstack('GM_2020', fill_value=0)[orden_marginacion[::-1]].stack().rename('GM_COUNT')
    # Para cada Sector calculamos el porcentaje de cada grupo en el Sector, pero acumulado en el orden 'orden_marginacion'
    # porque no supe como apilar las barras, por lo que serán dibujadas una detrás de otra, por eso necesito el acumulado
    datos = datos.groupby(level=col_regiones).transform(lambda x: (100*x/x.sum()).cumsum())
    # Regresamos el índice a columnas para tener (Sector, Grupo, Porcentaje acumulado)
    datos = datos.reset_index()

    # Graficamos las barras una detrás de la otra en el orden inverso para que sean visibles todas
    plt.xticks(rotation=90)
    ax = sns.barplot(datos, x=col_regiones, y='GM_COUNT', hue='GM_2020', hue_order=orden_marginacion, palette=paleta_marginacion, dodge=False)
    sns.move_legend(ax, "center left", bbox_to_anchor=(1, 0.5))
    ax.set(xlabel=TablaMarginacion.columnas[col_regiones]['descriptivo'], ylabel='% Marginación')
    plt.title('Proporción de grupos de marginación')
    plt.show()
    

