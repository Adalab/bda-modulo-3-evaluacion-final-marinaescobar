# LIBRERÍAS NECESARIAS

# Tratamiento de datos
import pandas as pd
import numpy as np
import re

# Imputación de nulos usando métodos avanzados estadísticos
from sklearn.impute import SimpleImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.impute import KNNImputer

# Evaluar linealidad de las relaciones entre las variables
import scipy.stats as stats
from scipy.stats import f_oneway


def open_file (ruta):
    
    """
    Lee un archivo CSV desde la ruta especificada y devuelve un DataFrame de pandas.

    Parámetros:
    ruta (str): La ruta del archivo CSV que se va a leer.

    Devoluciones:
    pandas.DataFrame: Un DataFrame que contiene los datos del archivo CSV.

    Ejemplo:
    df = apertura('archivo.csv')
    """
    
    df = pd.read_csv(ruta)

    # Si al cargar el dataframe se creó una columna de unnamed, la elimina
    if 'Unnamed: 0' in df.columns:
        df.drop('Unnamed: 0', axis = 1, inplace=True)
        
    return df


def exploration (df):
    
    """
    Realiza un análisis exploratorio de datos (EDA) en el DataFrame proporcionado e imprime varias informaciones.

    Parámetros:
    df (pandas.DataFrame): El DataFrame que se va a analizar.

    Esta función imprime la siguiente información sobre el DataFrame:
    - Forma: Número de filas y columnas.
    - Nombres de las columnas.
    - Tipos de datos.
    - Porcentaje de valores nulos para cada columna.
    - Número de filas duplicadas.
    - Recuento de valores únicos para cada valor único en cada columna.
    - Estadísticas resumidas para columnas numéricas.
    - Estadísticas resumidas para columnas categóricas.
    - Muestra de los primeros 10 elementos.
    - Muestra de 10 elementos aleatorios.
    - Muestra de los últimos 10 elementos.
    """
       
    print(f"INFORMACIÓN SOBRE EL DATAFRAME")
    
    print(f"---La forma:")
    print(f"{df.shape}\n")
    
    print(f"---Las columnas:")
    print(f"{df.columns}\n")
    
    print(f"---Los tipos de datos:")
    print(f"{df.dtypes}\n")
    
    print(f"---Los nulos:")
    print(f"{df.isnull().sum()/df.shape[0] * 100}\n")
    
    print(f"---Los duplicados:")
    print(f"{df.duplicated().sum()}\n")
    
    print(f"---Los valores únicos de cada columna:")
    for column in df.columns:
        print(f"-------{column.upper()}")
        print(f"{df[column].unique()}\n")
    
    print(f"---Los valores de cada columna y su total:")
    for column in df.columns:
        print(f"-------{column.upper()}")
        print(f"{df[column].value_counts()}\n")
        
    try:
        print(f"---Los principales estadísticos para las columnas numéricas:")
        display(df.describe().T)
    except:
        pass
    
    try:
        print(f"---Los principales estadísticos para las columnas categóricas:")
        display(df.describe(include=['object']).T)
    except:
        pass
    
    print(f"---Muestra de los 10 primeros elementos del DataFrame:")
    display(df.head(10))
    
    print(f"---Muestra de 10 elementos aleatorios del DataFrame:")
    display(df.sample(10))
    
    print(f"---Muestra de los 10 últimos elementos del DataFrame:")
    display(df.tail(10))


    
def union (df1, df2, columna_union):
    
    """
    Une dos DataFrames utilizando una columna común.

    Parámetros:
    df1 (DataFrame): El primer DataFrame a unir.
    df2 (DataFrame): El segundo DataFrame a unir.
    columna_union (str): El nombre de la columna común utilizada para unir los DataFrames.

    Retorna:
    DataFrame: Un nuevo DataFrame que resulta de la unión de df1 y df2 utilizando la columna especificada.

    Ejemplo:
    df_unido = union(df1=datos1,
                     df2=datos2,
                     columna_union='columna_comun')
    """
    
    df3 = pd.merge(df1, df2, on = columna_union)
    
    return df3


def data_cleaning (df):
    
    """
    Realiza la limpieza de datos en un DataFrame.

    Parámetros:
    df (DataFrame): El DataFrame que se va a limpiar.

    Retorna:
    DataFrame: El DataFrame después de realizar la limpieza de datos.

    Ejemplo:
    df_limpiado = data_cleaning(df)

    Operaciones realizadas:
    - Guarda las columnas categóricas en una lista.
    - Convierte los valores de las columnas categóricas a minúsculas, excepto 'Postal Code'.
    - Elimina filas duplicadas del DataFrame.
    - Convierte los números negativos en la columna 'Salary' a positivos.
    - Establece los nombres de las columnas en minúsculas y con guiones bajos.

    Consideraciones:
    - Los valores de las columnas categóricas se convierten a minúsculas solo si son de tipo 'str'.
    - La columna 'Salary' se ajusta para asegurar que todos los valores sean positivos.

    """
    
    # Guarda las columnas categóricas en una lista
    columns_cat = list(df.select_dtypes(include = 'object').columns)
           
    # Pone los datos de las columnas categóricas en minúsculas (a excepción del código postal), siempre y cuando el dato sea tipo string
    for column in columns_cat: 
        if column != 'Postal Code':
            df[column] = df[column].apply(lambda x: x.lower() if isinstance(x , str) else x)
        
    # Revisa y elimina los duplicados del df
    duplicates = df.duplicated().sum()
    if duplicates > 0:
        df.drop_duplicates(inplace = True)
    
    # Crea un diccionario con los meses y su nuevo nombre   
    months_name = {1 : '01-Jan',
                   2 : '02-Feb',
                   3 : '03-Mar',
                   4 : '04-Apr',
                   5 : '05-May',
                   6 : '06-Jun',
                   7 : '07-Jul',
                   8 : '08-Aug',
                   9 : '09-Sep',
                   10 : '10-Oct',
                   11 : '11-Nov',
                   12 : '12-Dec'}
    
    try:
        # Convierte los meses en número a sus abreviaturas
        df['Month'] = df['Month'].map(months_name)
    
    except:
        pass

    try:
        # Convierte los meses en número a sus abreviaturas
        df['Enrollment Month'] = df['Enrollment Month'].map(months_name)
    
    except:
        pass

    try:    
        # Convierte los números negativos de la columna 'Salary' a positivos
        df['Salary'] = df['Salary'].apply(lambda x: abs(x) if x < 0 else x)
    except:
        pass
        
    # Establece un diccionario con los nombres originales de las columnas y sus nuevos valores
    new_names = {column: column.lower().replace(' ', '_').strip() for column in df.columns}
    df.rename(columns = new_names, inplace = True)
    
    try:
        # Por último, elimina del df final aquellas filas que contengan un 0 en las columnas `flights_booked`, `flights_with_companion` y `total_flights`
        df = df[(df['flights_booked'] != 0) & (df['flights_with_companions'] != 0) & (df['total_flights'] != 0)]
    except:
        pass
    
    return df


def missing_data_imputation (df):
    
    """
    Realiza la imputación de datos faltantes en un DataFrame.

    Esta función detecta las columnas que contienen valores nulos en un DataFrame y realiza la imputación de estos valores 
    utilizando diferentes métodos dependiendo del porcentaje de valores nulos en cada columna.

    Parámetros:
    df (DataFrame): El DataFrame en el que se realizará la imputación de datos faltantes.

    Retorna:
    DataFrame: El DataFrame después de realizar la imputación de datos faltantes.

    Ejemplo:
    df_imputado = missing_data_imputation(df)

    Operaciones realizadas:
    - Crea una lista de columnas que contienen valores nulos.
    - Itera sobre cada columna de la lista.
    - Si el porcentaje de valores nulos en una columna es igual o superior al 60%, elimina la columna del DataFrame.
    - Si el porcentaje de valores nulos está entre el 15% y el 60%, prueba los métodos Iterative Imputer y KNN Imputer 
      para determinar cuál es más efectivo para la imputación.
    - Si el porcentaje de valores nulos es menor al 15%, utiliza la mediana para imputar los valores faltantes.

    Consideraciones:
    - La imputación de valores nulos se realiza inplace en el DataFrame original.

    """
    
    # Crea una lista de columnas que contienen valores nulos
    missing_value_columns = list(df.columns[df.isnull().any()])
    
    # Itera por cada columna de la lista de columnas nulas
    for column in missing_value_columns:
        
        # Establece una variable con el % de nulos que tiene la columna en cuestión
        missing_value_percentage = (df[column].isnull().sum() / df.shape[0]) * 100
        
        # Si el % de nulos es igual o superior a 60, elimina la columna del df
        if missing_value_percentage >= 60:
            print(f"Se ha eliminado la columna {column} del df debido a su elevado % de nulos ({round(missing_value_percentage , 2)}%)")
            df.drop(column , axis = 1 , inplace = True)
        
        # Si el % de nulos es igual o superior a 15, prueba con Iterative Imputer y KNN Imputer cuál es más eficaz para llevar a cabo la imputación
        elif missing_value_percentage >= 15:
            
            df_iterative = df.copy()
            df_knn = df.copy()
            
            # Prueba el método Iterative Imputer
            imputer_iterative = IterativeImputer(max_iter = 20, random_state = 42)
            imputer_iterative_imputed = imputer_iterative.fit_transform(df_iterative[[column]])
            df_iterative[column] = imputer_iterative_imputed
            median_iterative = df_iterative[column].median()
            mean_iterative = df_iterative[column].mean()
            iterative_difference = mean_iterative - median_iterative
            
            # Prueba el método KNN Imputer
            imputer_knn = KNNImputer(n_neighbors = 5)
            imputer_knn_imputed = imputer_knn.fit_transform(df_knn[[column]])
            df_knn[column] = imputer_knn_imputed
            median_knn = df_knn[column].median()
            mean_knn = df_knn[column].mean()
            knn_difference = mean_knn - median_knn
            
            # Si la diferencia entre media y mediana es mayor usando el método iterative, usaremos el KNN en el final
            if iterative_difference > knn_difference:
                print(f"El método escogido para imputar los nulos de {column} es: KNN Imputer")
                imputer_knn = KNNImputer(n_neighbors = 5)
                imputer_knn_imputed = imputer_knn.fit_transform(df[[column]])
                df[column] = np.round(imputer_knn_imputed, 2)
                
            # Por el contrario, si hay mayor diferencia entre media y mediana con el KNN, usaremos el iterative
            else:
                print(f"El método escogido para imputar los nulos de {column} es: Iterative Imputer")
                imputer_iterative = IterativeImputer(max_iter = 20, random_state = 42)
                imputer_iterative_imputed = imputer_iterative.fit_transform(df[[column]])
                df[column] = np.round(imputer_iterative_imputed, 2)
                
        # En el caso contrario (si el % de nulos es menor que 15), utiliza la mediana en la imputación de nulos
        else:
            median = df[column].median()
            df[column] = df[column].fillna(median)
            print(f"El método escogido para imputar los nulos de la columna {column} es: Reemplazo por la mediana ({median})")
            
    return df


def group_by_analysis (df , column_name):
    
    """
    Realiza un análisis de agrupación en un DataFrame.

    Parámetros:
    - df (DataFrame): El DataFrame que contiene los datos a analizar.
    - column_name (str): El nombre de la columna por la cual agrupar.

    Retorna:
    - summary_df (DataFrame): Un DataFrame con estadísticas resumidas para cada grupo.

    Esta función calcula estadísticas resumidas (media, desviación estándar, percentiles) 
    para cada grupo definido por los valores en la columna especificada.

    Ejemplo:
    summary_df = group_by_analysis(data_frame, 'Categoría')
    """
    
    # Crea un df con los datos agrupados por la columna escogida y muestra sus principales datos estadísticos
    # (total, media, desviación estándar, min, percentil 25, percentil 50 o mediana, percentil 75 y máximo)
    summary_df = df.groupby(column_name).describe()
    
    return summary_df


def anova_test (df , column_group_name, column_data_name):
    
    """
    Realiza un test de ANOVA para determinar si hay diferencias significativas
    entre los grupos definidos por una columna categórica en un DataFrame.

    Parámetros:
    - df (DataFrame): El DataFrame que contiene los datos a analizar.
    - column_group_name (str): El nombre de la columna que define los grupos.
    - column_data_name (str): El nombre de la columna que contiene los datos a comparar.

    Retorna:
    - f_statistic (float): El valor de la estadística F del test de ANOVA.
    - p_value (float): El valor p resultante del test de ANOVA.

    Esta función realiza un test de ANOVA para determinar si hay diferencias
    significativas entre los grupos definidos por una columna categórica en un DataFrame.
    Calcula la estadística F y el valor p del test de ANOVA y los retorna.

    Ejemplo de uso:
    f_stat, p_val = anova_test(df_eval, 'education', 'flights_booked')
    """
    
    # Extrae cada uno de los grupos usando column_name de referencia
    groups = df[column_group_name].unique()
    group_data = []
    
    # Obtiene los datos para cada grupo y los almacena en la lista group_data
    for group in groups:
        
        # Selecciona solo las filas donde el valor en la columna column_group_name coincide con el nombre del grupo actual
        # Y añade sólo los datos de la columna column_data_name
        group_data.append(df[df[column_group_name] == group][column_data_name])
        
    # Realiza el test de ANOVA (el * se utiliza para desempaquetar la secuencia de datos de la lista group_data)
    f_statistic, p_value = f_oneway(*group_data)
    
    # Interpreta los resultados
    alpha = 0.05
    if p_value < alpha:
        print(f"Se rechaza la hipótesis nula (H0).\nCon un p_value de {round(p_value,2)} hay una diferencia significativa entre los diferentes grupos")
    else:
        print(f"No se puede rechazar la hipótesis nula (H0).\nCon un p_value de {round(p_value,2)} no hay suficiente evidencia para afirmar que existe una diferencias significativas entre los distintos grupos")
    
    return p_value