"""
Simple script to get weather data from climate.weather.gc.ca programmatically.

More info: ftp://client_climate@ftp.tor.ec.gc.ca/Pub/Get_More_Data_Plus_de_donnees/Readme.txt
"""

import datetime

import requests


timeframes = {
    'hourly': 1,
    'daily': 2,
    'monthly': 3,
}

url = 'http://climate.weather.gc.ca/climate_data/bulk_data_e.html'
params = {
    'format': None,
    'stationID': 51157, # MONTREAL INTL A Station ID
    'Year': None,
    'Month': None,
    'Day': 1, # not used and can be an arbitrary value
    'timeframe': timeframes['daily'],
    'submit': 'Download Data',
}

params['Year'] = 2018
params['Month'] = 1
params['format'] = 'csv'

r = requests.get(url, params=params)

with open(f'data/2018-01.csv', 'w') as f:
    f.write(r.text)
