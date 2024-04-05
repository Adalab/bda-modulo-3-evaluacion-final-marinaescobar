## EDA

### Observaciones acerca del DataFrame 'Customer Flight Activity'

- Los nombres de las columnas son homogéneos, pero podrían cambiarse a minúsculas y sustituir espacios en blanco por '_'
- No existen columnas categóricas: Todas son tipo int64 a excepción de Points Accumulated que es float64
    - Revisar si se puede pasar a int o si contiene decimales relevantes
    - Hay algunos casos en los que sí existen decimales, como .25 o .75. En este caso se decide conservar el tipo float para convservar la precisión de los datos de cara a futuros análisis
- No hay nulos
- Existe una elevada cantidad de duplicados
    - ¿Son estos duplicados registros válidos?
- Se indagó en el significado de las columnas `flights booked`, `flights with companions` y `total flights`. Se llegó a la conclusión:
    - `flights booked` son aquellos vuelos que reservó el cliente para sí mismo
    - `flights with companion` son aquellos vuelos que reservó el cliente para otros usuarios
    - `total flights` es la suma de ambos
- Revisar en detalle aquellas columnas con un '0' entre sus valores: `flights booked`, `flights with companions`, `total flights`, `distance`, `points accumulated`, `points redeemed` y `dollar cost points redeemed`
- Existen algunas columnas cuya **media y mediana** se diferencian por bastante. Esas columnas son precisamente las que cuentan con '0' entre sus valores
- Tras observar el DataFrame, se aprecia que existen filas con un '0' en la mayoría de sus columnas. Estas filas no aportan ningún tipo de información relevante e influyen no sólo en la dispersión de los datos sino en el número de duplicados. Se concluye que en la fase de limpieza se prescindirá de dichas filas con tal de obtener una muestra final más homogénea y fiel a la realidad de cara a futuros análisis.

### Observaciones acerca del DataFrame 'Customer Loyalty History'

- Al igual que en el caso anterior, se aprecia que todos los nombres de columna son homogéneos, pero existe la posibilidad de ponerlos en minúscula y sustituir espacios en blanco por '_'
- A diferencia del anterior DF, en este caso sí hay columnas categóricas: `country`, `province`, `city`, `postal code`, `gender`, `education`, `marital status`, `loyalty card` y `enrollment type`
    - Tras una revisión se determina que no se puede convertir `postal code` a int, ya que contiene tanto letras como números
- No existen duplicados en este DF
- Hay dos columnas con un alto % de nulos (>87%), `cancellation year` y `cancellation month`, y una tercera con un % de nulos menor (>25%), `salary`
    - La imputación de nulos se llevará a cabo en `salary` para el análisis de los datos, pero se prescindirá de `cancellation year` y `cancellation month` al considerar que los datos no representarían correctamente la realidad, ya que en su inmensa mayoría serían imputados y no 
    - Al revisar los nulos de `salary` se observa que pertenecen a la categoría `Collegue` de la columna `Education`
- Los valores de las columnas categóricas también parecen homogéneos y sin erratas o símbolos especiales, pero de nuevo se podrían poner en minúsculas
- Revisar la existencia de salarios en negativo en la columna `salary` y cambiarlos a positivo
- En general las medias y medianas de las columnas numéricas no difieren demasiado, a excepción de las columnas `CLV` y `salary`
    - Info acerca del término 'CLV' o 'Customer Life Value': Podría entenderse como el valor neto que un cliente genera para la empresa a lo largo de toda su vida como cliente de la aerolínea
    - Puede que esto se deba a los negativos de `salary`, revisar de nuevo una vez que se hayan convertido a positivos

### Observaciones generales

- El punto de unión de ambos DF es la columna `Loyalty Number` y dado que el DF `Customer Flight Activity` cuenta con registros en lugar de valores únicos, se usará como base para anexionar los datos de `Customer Loyalty History`

## Data Transformation

### Decisiones sobre la limpieza

A partir de lo observado durante la fase de EDA, se ha hecho una limpieza del df (resultante de la unión entre `Customer Flight Activity`y `Customer Loyalty History`) tomando en cuenta:

- Que los valores de las columnas categóricas, salvo `postal_code`, estuvieran en minúsculas
- Que aquellas filas duplicadas se eliminaran del df para evitar análisis posteriores con resultados erróneos
- Que todos los números de la columna `salary` se convirtieran a positivos, ya que se entiende que aquellos negativos se deben a un error pues no existen salarios en negativo (de momento)
- Que todas aquellas filas cuyo valor en `flights_booked`, `flights_with_companions` y `total_flights` fuera 0, se eliminaran del df definitivo, ya que eran datos que no representaban ningún valor para el análisis y afectaban negativamente a la dispersión de los datos de columnas como `points_accumulated`
- Que los nombres de las columnas pasaran a estar en minúscula y con "_" en lugar de espacios
- Que las columnas con los meses en numérico se reemplazarían por sus abreviaturas para mayor claridad en los análisis

### Decisiones sobre la imputación de nulos

A partir de lo observado durante la fase de EDA, se han tomado las siguientes decisiones respecto a la eliminación y/o imputación de los nulos:

- Que aquellas columnas con un % de nulos superior o igual al 60% (`cancellation_year` y `cancellation_month`) se eliminaran del df final al no poder reflejar la realidad de los clientes dado al elevado % de nulos que poseían (>80%)
- Que en la columna `salary`, cuyo % de nulos rondaba el 25% y afectaba únicamente a la categoría `collegue` de la columna `education`, se realizaría una imputación de nulos para poder comparar posteriormente el salario promedio entre los diferentes niveles educativos de los clientes (de este modo la categoría `collegue` sí podrá ser contemplada en el análisis, aunque se informará de que sus datos han sido imputados)
    - Esta imputación se ha llevado a cabo usando el método Iterative Imputer, ya que es el que generaba una menor diferencia entre la media y la mediana de la columna