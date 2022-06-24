# OptimalGo Project

![portada](https://www.seguritecnia.es/wp-content/uploads/2021/06/relacion-entre-logistica-y-tecnologia-1200x800.jpg)

El Proyecto **OptimalGo** tiene como objetivo pronosticar los envíos de paquetería que se realizan entre particulares en las diferentes provincias españolas.

Con este fin, se calcularon 50 series temporales para cada una de las 50 provincias que dispone el territorio español. Después de probar diferentes modelos, tanto de series temporales como regresiones lineales, el modelo que mejor resultado obtuvo durante las pruebas fue [Prophet](https://facebook.github.io/prophet/), obteniendo un RMSE y MAPE más optimo que el resto de los modelos. 

      
## Estructura de carpetas 

- **Notebook:** Se encuentran los archivos .ipynb donde podemos encontrar el modelo utilizado, la fusión de los csv, geopy y la inserción de datos en Mongo DB.

- **Data:** se encuentras los archivos csv. Solo se dispone de algunos csv por el límite de tamaño que nos permite Github.

- **Src:** Se encuentran las funciones utilizadas en los notebook.


## Medidas adoptadas

1. Limpieza del conjunto de datos y análisis exploratorio del mismo.

2. Web Scraping de los festivos del 2018-2022 para poder entender los envíos en días festivos en según que provincia.

3. Cálculos y comparación de los diferentes modelos.

4. Crear pronósticos para las 50 provincias (2.500 series).

5. Fusión de los csv.

6. Generar las coordenadas de las provincias con Geopy.

7. Insertar los datos en MongoDB.

## Librerías

En este proyecto se han utilizado las siguientes bibliotecas:

- Pandas
- Numpy
- Stastsmodels
- Sys
- Os
- Tqdm
- Geopy
- pymongo
- Fbprophet
