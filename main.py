#%%
# Importaciones de funciones
from src import functions as fun
from src import visualization as vis

# Librerías de tratamiento de datos
import pandas as pd

# Configuración
pd.set_option('display.max_columns', None) # para poder visualizar todas las columnas de los DataFrames

# -------------------------------------------------- FASE 1: EXPLORACIÓN Y LIMPIEZA

# -------------------------------------------------- Apertura de archivos
#%%
# Apertura del df 'Customer Flight Activity'
df_FA = fun.open_file('files\Customer Flight Activity.csv')

# Apertura del df 'Customer Loyalty History'
df_LH = fun.open_file('files\Customer Loyalty History.csv')

# -------------------------------------------------- Exploración de los DFs
#%%
# Exploración del df 'Customer Flight Activity'
fun.exploration(df_FA)

# %%
# Revisión específica para las filas duplicadas en la que se observa que son aquellas cuyos valores en la mayoría de columnas equivalen a 0
duplicated_rows = df_FA[df_FA.duplicated()]
duplicated_rows.sample(10)

#%%
# Exploración del df 'Customer Loyalty History'
fun.exploration(df_LH)

#%%
# Revisión específica para las filas que tienen nulos en la columna de `salary`
missing_data_rows = df_LH[df_LH['Salary'].isnull()]
display(missing_data_rows.sample(10))
print(df_LH.loc[df_LH['Salary'].isnull(), 'Education'].unique())

# -------------------------------------------------- Limpieza de los DFs
#%%
# Elimina duplicados y homogeiniza criterios
df_FA_clean = fun.data_cleaning(df_FA) 
df_LH_clean = fun.data_cleaning(df_LH) 

# -------------------------------------------------- Imputación de nulos 
#%%
# Imputación de nulos para el df 'Customer Loyalty History' 
# (esta ejecución puede tardar unos min debido a que realiza una serie de comprobaciones antes de llevar a cabo la imputación)
df_LH_no_nulls = fun.missing_data_imputation(df_LH_clean)

# -------------------------------------------------- Unión de ambos DFs
#%%
# Unión de ambos DF usando la columna 'Loyalty Number' como referente
df = fun.union(df_FA_clean , df_LH_no_nulls, 'loyalty_number')

# -------------------------------------------------- Exploración del df resultante
#%%
# Revisión del DF para verificar los cambios
fun.exploration(df)

# -------------------------------------------------- FASE 2: VISUALIZACIÓN

# -------------------------------------------------- Distribución de la cantidad de vuelos reservados por mes durante el año
#%%
flights_by_month_year = df.groupby(['year', 'month'])['flights_booked'].sum().reset_index()

vis.barplot('month', 'flights_booked', flights_by_month_year, 'Set3', 'year', 'Year', True, 'Month', 'Total flights booked', 'Distribution of Flights Booked per Month', (14,6))

#Observaciones: Existe una mayor concentración de vuelos reservados en los meses de verano (junio, julio y agosto) para ambos años, así como un leve despunte en el mes de diciembre
                # También se aprecia que en el año 2018 hubieron más reservas de mayo a diciembre que en las mismas fechas de 2017 

# -------------------------------------------------- Relación entre la distancia del vuelo y los puntos acumulados por el cliente
#%%
vis.scatter(df['distance'], df['points_accumulated'], 'orchid', 20, 'Flight Distance', 'Accumulated Points', 'Relationship between Flight Distance and Accumulated Points', 0.8, (8,6))

#Observaciones: Existe una clara relación entre la distancia recorrida en el vuelo y el número de puntos acumulados
#               # Esta relación, además, parece ser de tendencia positiva, pues cuando una de ambas variables aumenta, la otra también

# -------------------------------------------------- Distribución de los clientes por provincia o estado
#%%
vis.countplot('province', df, 'Purples', False, None, False, 'Province', 'Total Clients', 'Distribution of Total Clients per Province', 45, (8,6))

#Observaciones: No existe una representación uniforme de las provincias, sino que se aprecia que la gran mayoría de clientes pertenece a Ontario, 
                # seguidos por British Columnia. Por contra, Prince Edward Island tiene la menor representación

# -------------------------------------------------- Comparación del salario promedio entre los diferentes niveles educativos de los clientes
#%%
vis.barplot('education', 'salary', df, 'BuPu_r', 'education', None, False, 'Education Level', 'Average Salary', 'Comparison of Average Salary by Education Level', (8,6))

#Observaciones: Hay que tener en cuenta que los datos de College se imputaron para que pudiera tener representación en la gráfica, ya que para esta categoría no existía ningún registro de valores
                # Sin embargo, estos datos deberán cogerse con pinzas ya que no servirían para establecer conclusiones firmes. Se necesitaría recibir los datos reales para ello
                # Teniendo esto en cuenta, se aprecia que cuanto mayor es el nivel educativo, mayor promedio salarial
                # También cabe destacar que la dispersión estándar de la columna `salary` es bastante elevada, lo cual indica la presencia de valores atípicos que 
                # en un futuro análisis se podrían estudiar aparte y con mayor nivel de detalle (dada la eleavada diferencia de salario en los doctorado respecto al resto de niveles educativos, es posible que en esa categoría se condensen los outliers)

# -------------------------------------------------- Proporción de clientes con diferentes tipos de tarjetas de fidelidad
#%%
vis.pie(df['loyalty_card'].value_counts(), df['loyalty_card'].value_counts().index, 15, 'white', None, 'BuPu_r', 'Percentage of clients for each Loyalty Card', 'black', 14, 0.05, (6,6))

#Observaciones: La mayoría de clientes se mueven entre las tarjetas de fidelidad star y nova (con un 45,5% y 33,9% respectivamente), 
                # siendo aurora la que menor representación tiene (20,6%)

# -------------------------------------------------- Distribución de los clientes según su estado civil y su género
# %%
vis.countplot('marital_status', df, 'Purples', 'gender', True, True, 'Marital Status', 'Total Clients', 'Distribution of Total Clients per Marital Status', 0, (8,6))

#Observaciones: No existe una diferencia entre ambos géneros en lo que a estado civil respecta
                # Lo que sí se observa es que la mayoría de clientes de la aerolínea (tanto hombres, como mujeres) están casados

# -------------------------------------------------- FASE 3: EVALUACIÓN 

# -------------------------------------------------- Filtrado del conjunto de daots para incluir `flights_booked` y `education`
#%%
df_eval = df[['flights_booked', 'education']]

# -------------------------------------------------- Análisis descriptivo
#%%
summary_df = fun.group_by_analysis(df_eval , 'education')
display(summary_df)

vis.boxplot('education' , 'flights_booked', df_eval, 'BuPu_r', 'education', None, False, 'Education level', 'Average Flights Booked', 'Distribution of Avg. Flights Booked per Education Level', (7,6))

# Observaciones: Los diferentes niveles educativos tienen una cantidad similar de vuelos reservados, con medias cercanas a 8 vuelos
                # Las diferencias en la desviación estándar sugieren que la cantidad de vuelos reservados varía poco en cada grupo (siendo `high school or below` los más dispersos) 
                # Los percentiles muestran que la mayoría de los clientes reservan entre 4 y 11 vuelos
                # No obstante, la alta homogeneidad de la muestra es algo curioso: estaría bien revisar el método de obtención de datos por si acaso

# -------------------------------------------------- Prueba estadística
#%%
# Revisión de normalidad de los datos
fun.normality_kolmogorov(df_eval, 'education', 'flights_booked')
#Observaciones: La columna `flights_booked` no sigue una distribución normal en ninguno de los grupos de 'education'
print("-----------------------------------------------------------")
# Revisión de homogeneidad de los datos
fun.homogeneity_of_variances(df_eval, 'education', 'flights_booked')
#Observaciones: La columna `flights_booked` sigue una distribución homogénea para los grupos de 'education'

#%%
# Hipótesis general:
# ----- Hipótesis nula (H0): No hay diferencia significativa en el número de vuelos reservados entre los diferentes niveles educativos
# ----- Hipótesis alternativa (H1): Existe al menos una diferencia significativa en el número de vuelos reservados entre los diferentes niveles educativos

# Método de análisis escogido: Test de Kruskal-Wallis
# ----- La razón principal para utilizar este método no paramétrico es porque la muestra de datos no cumple con el criterio de normalidad
        # También porque permite comparar las medianas de tres o más grupos independientes
p_value = fun.kruskal_wallis_test(df_eval, 'education', 'flights_booked')

#Observaciones: Dado que el p_value obtenido en el test es de 0.68, no se puede descartar la hipótesis nula (h0)
                # Por tanto, no existe diferencia significativa en el número de vuelos reservados entre los diferentes niveles educativos