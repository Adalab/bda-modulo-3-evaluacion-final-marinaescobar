# LIBRERÍAS NECESARIAS

# Tratamiento de datos
import pandas as pd
import numpy as np

# Visualización
import matplotlib.pyplot as plt
import seaborn as sns


def histplot (x_value, data_value, color_value , kde_value , bins_value, x_label, y_label, title_value, size = (10 , 6)):
    
    """
    Crea un gráfico de histograma utilizando Seaborn.

    Parámetros:
    x_value (str): Nombre de la columna en los datos a utilizar en el eje x.
    data_value (DataFrame): Los datos que se utilizarán para crear el gráfico.
    color_value (str): Color del histograma.
    kde_value (bool): Si se debe trazar o no la estimación de la densidad del núcleo (KDE).
    bins_value (int): Número de contenedores para el histograma.
    x_label (str): Etiqueta del eje x.
    y_label (str): Etiqueta del eje y.
    title_value (str): Título del gráfico.

    Retorna:
    None: El gráfico se muestra directamente en la salida.

    Ejemplo:
    histplot(x_value='columna1',
             data_value=datos,
             color_value='blue',
             kde_value=True,
             bins_value=20,
             x_label='Valores',
             y_label='Frecuencia',
             title_value='Histograma de Columna 1')
    """
    
    plt.figure(figsize= size)
    
    sns.histplot(x = x_value, 
             data = data_value, 
             color = color_value, 
             kde = kde_value, 
             bins = bins_value)
    
    plt.xlabel(x_label)
    
    plt.ylabel(y_label)
    
    plt.title(title_value);
    

def hist (x_value, data_value, color_value , edge_color_value, density_value , bins_value, x_label, y_label, title_value, size = (10 , 6)):
    
    """
    Crea un gráfico de histograma utilizando Matplotlib.

    Parámetros:
    x_value (array-like or list-like): Valores a representar en el eje x.
    data_value (DataFrame): Los datos que se utilizarán para crear el gráfico.
    color_value (str): Color de las barras del histograma.
    edge_color_value (str): Color del borde de las barras del histograma.
    density_value (bool): Si se debe normalizar el histograma a densidad 1.
    bins_value (int or sequence): Número de contenedores para el histograma o una secuencia de bordes de bin.
    x_label (str): Etiqueta del eje x.
    y_label (str): Etiqueta del eje y.
    title_value (str): Título del gráfico.

    Retorna:
    None: El gráfico se muestra directamente en la salida.

    Ejemplo:
    hist(x_value=datos['columna1'],
         data_value=datos,
         color_value='blue',
         edge_color_value='black',
         density_value=True,
         bins_value=20,
         x_label='Valores',
         y_label='Densidad',
         title_value='Histograma de Columna 1')
    """
    plt.figure(figsize= size)
    
    plt.hist(x = x_value, 
             data = data_value, 
             color = color_value,
             edgecolor =  edge_color_value,
             density = density_value, 
             bins = bins_value)
    
    plt.xlabel(x_label)
    
    plt.ylabel(y_label)
    
    plt.title(title_value);
    

def barplot (x_value, y_value, data_value, palette_value , hue_value, legend_title, show_legend, x_label, y_label, title_value, size = (10 , 6)):
    
    """
    Crea un gráfico de barras utilizando Seaborn.

    Parámetros:
    - x_value: Nombre de la columna en el DataFrame que se utilizará en el eje x.
    - y_value: Nombre de la columna en el DataFrame que se utilizará en el eje y.
    - data_value: DataFrame que contiene los datos a graficar.
    - palette_value: Paleta de colores a utilizar en las barras.
    - hue_value: Nombre de la columna en el DataFrame para agrupar y colorear las barras.
    - legend_title: Título de la leyenda del gráfico.
    - x_label: Etiqueta del eje x.
    - y_label: Etiqueta del eje y.
    - title_value: Título del gráfico.
    - size: Tamaño de la figura del gráfico (opcional, por defecto es (10, 6)).

    Retorna:
    No retorna ningún valor. Muestra el gráfico de barras.

    Esta función utiliza Seaborn para crear un gráfico de barras a partir de los datos proporcionados.
    Permite especificar el eje x, el eje y, la paleta de colores, la agrupación por categoría y la inclusión de una leyenda.

    Ejemplo de uso:
    barplot(x_value='Year', 
            y_value='Revenue', 
            data_value=yearly_data, 
            palette_value='Blues', 
            hue_value='Category', 
            legend_title='Product Category', 
            x_label='Año', 
            y_label='Ingresos', 
            title_value='Ingresos Anuales por Categoría de Producto',
            size=(12, 8))
    """
    
    plt.figure(figsize= size)
    
    sns.barplot(data = data_value, 
                x = x_value, 
                y = y_value, 
                hue = hue_value, 
                palette = palette_value)
    
    if show_legend and hue_value:
        plt.legend(title=legend_title)
        
    plt.title(title_value)
    plt.xlabel(x_label)
    plt.ylabel(y_label);
    
    
def scatter (x_value, y_value, dots_color, dots_size, x_label, y_label, title_value, dots_transparency = 0.7, size = (10 , 6)):
    
    """
    Crea un gráfico de dispersión utilizando Matplotlib.

    Parámetros:
    - x_value: Valores para el eje x.
    - y_value: Valores para el eje y.
    - dots_color: Color de los puntos del gráfico de dispersión.
    - dots_size: Tamaño de los puntos del gráfico de dispersión.
    - x_label: Etiqueta del eje x.
    - y_label: Etiqueta del eje y.
    - title_value: Título del gráfico.
    - dots_transparency: Transparencia de los puntos (opcional, por defecto es 0.7).
    - size: Tamaño de la figura del gráfico (opcional, por defecto es (10, 6)).

    Retorna:
    No retorna ningún valor. Muestra el gráfico de dispersión.

    Esta función utiliza Matplotlib para crear un gráfico de dispersión a partir de los datos proporcionados.
    Permite especificar los valores en los ejes x e y, el color y el tamaño de los puntos, así como las etiquetas
    de los ejes y el título del gráfico.

    Ejemplo de uso:
    scatter(x_value=data['Altura'], 
            y_value=data['Peso'], 
            dots_color='blue', 
            dots_size=30, 
            x_label='Altura (cm)', 
            y_label='Peso (kg)', 
            title_value='Relación entre Altura y Peso',
            dots_transparency=0.5,
            size=(8, 6))
    """
    
    plt.figure(figsize= size) 
    plt.scatter(x_value, 
                y_value, 
                color = dots_color,
                s = dots_size,
                alpha = dots_transparency)  

    plt.title(title_value)
    plt.xlabel(x_label)
    plt.ylabel(y_label);
    

def countplot (x_value, data_value, palette_value , hue_value, legend_title, show_legend, x_label, y_label, title_value, x_label_rotation = 0, size = (10 , 6)):

    """
    Crea un gráfico de conteo utilizando Seaborn.

    Parámetros:
    - x_value: Nombre de la columna en el DataFrame que se utilizará en el eje x.
    - data_value: DataFrame que contiene los datos a graficar.
    - palette_value: Paleta de colores a utilizar en las barras.
    - hue_value: Nombre de la columna en el DataFrame para agrupar y colorear las barras.
    - legend_title: Título de la leyenda del gráfico.
    - x_label: Etiqueta del eje x.
    - y_label: Etiqueta del eje y.
    - title_value: Título del gráfico.
    - x_label_rotation: Rotación de las etiquetas del eje x (opcional, por defecto es 0).
    - size: Tamaño de la figura del gráfico (opcional, por defecto es (10, 6)).

    Retorna:
    No retorna ningún valor. Muestra el gráfico de conteo.

    Esta función utiliza Seaborn para crear un gráfico de conteo a partir de los datos proporcionados.
    Permite especificar la columna en el eje x, la paleta de colores, la agrupación por categoría y la inclusión de una leyenda.

    Ejemplo de uso:
    countplot(x_value='Category', 
            data_value=category_data, 
            palette_value='Set2', 
            hue_value='Region', 
            legend_title='Region', 
            x_label='Categoría', 
            y_label='Cantidad', 
            title_value='Cantidad de Categorías por Región',
            x_label_rotation=45,
            size=(8, 6))
    """

    plt.figure(figsize= size)
    
    sns.countplot(x = x_value, 
                  data = data_value, 
                  palette = palette_value,
                  hue = hue_value,
                  legend = legend_title) 
    
    if show_legend and hue_value:
        plt.legend(title=legend_title)
        
    plt.title(title_value)
    plt.xlabel(x_label)
    plt.xticks(rotation = x_label_rotation)  
    plt.ylabel(y_label);


def pie (x_value, labels_value, labels_size, labels_color, data_value, palette_value, title_value, title_color, title_size, sep_number = 0.1, size = (8 , 8)):
    
    """
    Crea un gráfico de pastel utilizando Matplotlib.

    Parámetros:
    - x_value: Lista de valores numéricos que representan las proporciones de las porciones del pastel.
    - labels_value: Lista de etiquetas para las porciones del pastel.
    - labels_size: Tamaño de las etiquetas de las porciones del pastel.
    - labels_color: Color de las etiquetas de las porciones del pastel.
    - data_value: DataFrame que contiene los datos a graficar.
    - palette_value: Paleta de colores a utilizar en el pastel.
    - title_value: Título del gráfico.
    - title_color: Color del título del gráfico.
    - title_size: Tamaño del título del gráfico.
    - sep_number: Separación entre las porciones del pastel (opcional, por defecto es 0.1).
    - size: Tamaño de la figura del gráfico (opcional, por defecto es (8, 8)).

    Retorna:
    No retorna ningún valor. Muestra el gráfico de pastel.

    Esta función utiliza Matplotlib para crear un gráfico de pastel a partir de los datos proporcionados.
    Permite especificar las proporciones, etiquetas, colores y otras propiedades visuales del gráfico.

    Ejemplo de uso:
    pie(x_value=[40, 30, 20, 10], 
        labels_value=['A', 'B', 'C', 'D'], 
        labels_size=12, 
        labels_color='white', 
        data_value=category_data, 
        palette_value='Set2', 
        title_value='Distribución de Categorías', 
        title_color='blue', 
        title_size=16,
        sep_number=0.2,
        size=(8, 8))
    """
    
    proporcion = list(labels_value)
    separacion = [sep_number] * len(proporcion) 
    
    plt.figure(figsize= size)

    plt.pie(x_value, 
            labels = labels_value,
            autopct =  '%1.1f%%', 
            colors = sns.color_palette(palette_value, len(proporcion)), 
            textprops = {'fontsize': labels_size, 
                         'color' : labels_color}, 
            explode = separacion);
    
    plt.title(title_value, 
              color = title_color, 
              fontsize = title_size)
    plt.legend(bbox_to_anchor=(1.2, 1));
    
    
def boxplot(x_value, y_value, data_value, palette_value, hue_value, legend_title, show_legend, x_label, y_label, title_value, size=(10, 6)):
    
    """
    Crea un gráfico de cajas (boxplot) utilizando Seaborn.

    Parámetros:
    - x_value: Nombre de la columna en el DataFrame que se utilizará en el eje x.
    - y_value: Nombre de la columna en el DataFrame que se utilizará en el eje y.
    - data_value: DataFrame que contiene los datos a graficar.
    - palette_value: Paleta de colores a utilizar en el boxplot.
    - hue_value: Nombre de la columna en el DataFrame para agrupar y colorear las cajas.
    - legend_title: Título de la leyenda del gráfico.
    - x_label: Etiqueta del eje x.
    - y_label: Etiqueta del eje y.
    - title_value: Título del gráfico.
    - size: Tamaño de la figura del gráfico (opcional, por defecto es (10, 6)).

    Retorna:
    No retorna ningún valor. Muestra el gráfico de cajas.

    Esta función utiliza Seaborn para crear un gráfico de cajas a partir de los datos proporcionados.
    Permite especificar el eje x, el eje y, la paleta de colores, la agrupación por categoría y la inclusión de una leyenda.

    Ejemplo de uso:
    boxplot(x_value='Year', 
            y_value='Revenue', 
            data_value=yearly_data, 
            palette_value='Blues', 
            hue_value='Category', 
            legend_title='Product Category', 
            x_label='Año', 
            y_label='Ingresos', 
            title_value='Ingresos Anuales por Categoría de Producto',
            size=(12, 8))
    """

    plt.figure(figsize=size)
    
    sns.boxplot(data = data_value, 
                x = x_value, 
                y = y_value, 
                hue = hue_value, 
                palette = palette_value)
    
    if show_legend and hue_value:
        plt.legend(title=legend_title)
    
    plt.title(title_value)
    plt.xlabel(x_label)
    plt.ylabel(y_label);
    
