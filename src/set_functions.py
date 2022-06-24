import os
import pandas as pd
from geopy.geocoders import Nominatim 
geolocator = Nominatim(user_agent="Christian")
import fbprophet
from fbprophet import Prophet
import numpy as np


def concat_csv():
    '''
    Uso de la librería "os" para la carga de todos los csv que tenemos almacenadas en una ruta especifica.
    
        Returns:
               dataframe concatenado con la totalidad de registros extraídos.
    '''

    path = "/mnt/c/Users/chris/Ironhack/OptimalGo-project/Data/csv_provinces"
    filesname = os.listdir(path)
    all_df =[]

    for file in filesname:
        csv_prov = os.path.join(path, file)
        df_prov = pd.read_csv(f"{csv_prov}")
        all_df.append(df_prov)
    all_dataset = pd.concat(all_df, axis=0, ignore_index=True)
    # all_dataset.to_csv("../Data/merged_dataset.csv", index=False)
    return all_dataset


def coordenadas(x):
    location = geolocator.geocode(x)
    x = (location.latitude, location.longitude)
    return x


def holidays(df):
    list_fest = df[df['festivo'] == 1]['ds'].tolist()
    festivos = pd.DataFrame({"holiday": "temp season",
                             "ds": pd.to_datetime(list_fest),
                            "lower_window": 0, "upper_window": 1})
    return festivos

def model_prophet(df)
    prov_re = df['prov_re'].unique().tolist()
    prov_en = df['prov_en'].unique().tolist()
    for p_re in tqdm(prov_re): # provincia origen

        df_all = pd.DataFrame()

        for p_en in prov_en: # provincia destino

            try:

                df2 = df[(df['prov_re']  == p_re) & (df['prov_en']  == p_en)].reset_index()[2:]
                df2 = df2[['fecha', 'envios', 'festivo']]
                df2.columns = ["ds", "y", 'festivo']

                # modelo lunes a viernes
                model = Prophet(holidays= holidays(df2), holidays_prior_scale=1000, yearly_seasonality= 500).fit(df2)
                future = model.make_future_dataframe(periods = 215, freq = "D") # predicción 3 meses
                future = future[(future['ds'].dt.dayofweek != 6) & (future['ds'].dt.dayofweek != 5)]
                forecast = model.predict(future)
                forecast = forecast[["ds", "yhat","yhat_lower", "yhat_upper", "trend"]]
                forecast[["yhat","yhat_lower", "yhat_upper", "trend"]] = forecast[["yhat","yhat_lower", "yhat_upper", "trend"]].apply(lambda x: round(x))
                forecast['prov_re'] = p_re 
                forecast['prov_en'] = p_en
                df2 = df2[(df2['ds'].dt.dayofweek != 6) & (df2['ds'].dt.dayofweek != 5)].reset_index()
                df2 = df2[['y', 'festivo']]
                df_join = forecast.join(df2)
                df_join = df_join[df_join['festivo'] != 1]
                df_all = pd.concat([df_all, df_join], axis=0, ignore_index=True)

            except:
                pass

        filename = p_re
        df_all.to_csv(filename+'.csv', index=False)