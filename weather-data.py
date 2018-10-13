"""
Simple script to get weather data from climate.weather.gc.ca programmatically.

More info: ftp://ftp.tor.ec.gc.ca/Pub/Get_More_Data_Plus_de_donnees/Readme.txt
"""

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
    'Year': 2018,
    'Month': 1,
    'Day': 1, # not used and can be an arbitrary value
    'timeframe': timeframes['daily'],
    'submit': 'Download Data',
}

for format in ['csv', 'xml']:
    params['format'] = format
    r = requests.get(url, params=params)

    with open(f'weather-data.{format}', 'w') as f:
        f.write(r.text)
