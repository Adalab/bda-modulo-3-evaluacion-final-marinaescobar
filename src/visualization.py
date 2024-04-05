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
    

def barplot (x_value, y_value, data_value, palette_value , hue_value, legend_title, x_label, y_label, title_value, size = (10 , 6)):
    
    plt.figure(figsize= size)
    
    sns.barplot(data = data_value, 
                x = x_value, 
                y = y_value, 
                hue = hue_value, 
                palette = palette_value)
    plt.title(title_value)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    if legend_title is not None:
        plt.legend(title= legend_title)
    else:
        plt.legend().remove();
    
    
def scatter (x_value, y_value, dots_color, dots_size, x_label, y_label, title_value, dots_transparency = 0.7, size = (10 , 6)):
    
    plt.figure(figsize= size) 
    plt.scatter(x_value, 
                y_value, 
                color = dots_color,
                s = dots_size,
                alpha = dots_transparency)  

    plt.title(title_value)
    plt.xlabel(x_label)
    plt.ylabel(y_label);
    

def countplot (x_value, data_value, palette_value , hue_value, legend_title, x_label, y_label, title_value, x_label_rotation = 0, size = (10 , 6)):

    plt.figure(figsize= size)
    
    sns.countplot(x = x_value, 
                  data = data_value, 
                  palette = palette_value,
                  hue = hue_value,
                  legend = legend_title) 

    plt.title(title_value)
    plt.xlabel(x_label)
    plt.xticks(rotation = x_label_rotation)  
    plt.ylabel(y_label);



def pie (x_value, labels_value, labels_size, labels_color, data_value, palette_value, title_value, title_color, title_size, sep_number = 0.1, size = (8 , 8)):
    
    proporcion = list(labels_value)
    separacion = [sep_number] * len(proporcion) 
    
    plt.figure(figsize= size)

    plt.pie(x_value, 
            labels = labels_value,
            autopct =  '%1.1f%%', 
            colors = sns.color_palette(palette_value, len(proporcion)), 
            textprops = {'fontsize': labels_size, 'color' : labels_color}, 
            explode = separacion);
    
    plt.title(title_value, color = title_color, fontsize = title_size)
    plt.legend(bbox_to_anchor=(1.2, 1))
    
