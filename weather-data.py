"""
Simple script to get weather data from climate.weather.gc.ca programmatically.

More info: ftp://client_climate@ftp.tor.ec.gc.ca/Pub/Get_More_Data_Plus_de_donnees/Readme.txt
"""

import datetime

import requests


now = datetime.datetime.now()

start_year = 2018
start_month = 4


def get_year_month():
    year = start_year
    month = month_counter = start_month
    while year < now.year or (year == now.year and month <= now.month):
        yield year, month
        month_counter += 1
        month = ((month_counter - 1) % 12) + 1
        year = start_year + ((month_counter - 1) // 12)


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
    'timeframe': timeframes['hourly'],
    'submit': 'Download Data',
}

for year, month in get_year_month():
    params['Year'] = year
    params['Month'] = month
    for format in ['csv', 'xml']:
        params['format'] = format
        r = requests.get(url, params=params)

        with open(f'data/{year}-{month}.{format}', 'w') as f:
            f.write(r.text)
