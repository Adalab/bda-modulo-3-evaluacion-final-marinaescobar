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
flights_by_month_year = df.groupby(['year', 'month'])['total_flights'].sum().reset_index()

vis.barplot('month', 'total_flights', flights_by_month_year, 'Set3', 'year', 'year', 'Month', 'Total flights booked', 'Distribution of Total Flights per Month', (14,6))

#Observaciones: Existe una mayor concentración de vuelos reservados en los meses de verano (junio, julio y agosto) para ambos años, así como un leve despunte en el mes de diciembre

# -------------------------------------------------- Relación entre la distancia del vuelo y los puntos acumulados por el cliente
#%%
vis.scatter(df['distance'], df['points_accumulated'], 'orchid', 20, 'Flight Distance', 'Accumulated Points', 'Relationship between Flight Distance and Accumulated Points', 0.8, (10,6))

#Observaciones: Existe una clara relación entre la distancia recorrida en el vuelo y el número de puntos acumulados. Esta relación, además, parece ser de tendencia positiva, pues cuando una de ambas variables aumenta, la otra también

# -------------------------------------------------- Distribución de los clientes por provincia o estado
#%%
vis.countplot('province', df, 'Purples', False, False, 'Province', 'Total Clients', 'Distribution of Total Clients per Province', 45, (8,6))

#Observaciones: No existe una representación uniforme de las provincias, sino que se aprecia que la gran mayoría de clientes pertenece a Ontario, seguidos por British Columnia. Por contra, Prince Edward Island tiene la menor representación

# -------------------------------------------------- Comparación del salario promedio entre los diferentes niveles educativos de los clientes
#%%
vis.barplot('education', 'salary', df, 'BuPu_r', False, None, 'Education Level', 'Average Salary', 'Comparison of Average Salary by Education Level', (10,6))

#Observaciones: Hay que tener en cuenta que los datos de College se imputaron para que pudiera tener representación en la gráfica, ya que para esta categoría no existía ningún registro de valores
                # Sin embargo, estos datos deberán cogerse con pinzas ya que no servirían para establecer conclusiones firmes. Se necesitaría recibir los datos reales para ello
                # Teniendo esto en cuenta, se aprecia que cuanto mayor es el nivel educativo, mayor promedio salarial
                # Especial mención al grado de doctorado, cuyo promedio es muy superior al resto

# -------------------------------------------------- Proporción de clientes con diferentes tipos de tarjetas de fidelidad
#%%
vis.pie(df['loyalty_card'].value_counts(), df['loyalty_card'].unique(), 15, 'white', None, 'BuPu_r', 'Prueba', 'white', 20, 0.1, (7,7))


# %%
