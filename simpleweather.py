#!/usr/bin/python3
# OpenWeatherMap Temperature Only

import json
from urllib.request import urlopen

# Add your OpenWeatherMap API key below.
APIKEY = ''
ZIPCODE = '59701'
# Use either 'imperial' or 'metric' below for units.
# Imperial gives you the temperature in fahreinheit and metric gives you celsius.
UNITS = 'imperial'

if APIKEY = '':
    print('Please edit simpleweather.py and add your OpenWeatherMap API key.')
    exit()

try:
    URL = urlopen('https://api.openweathermap.org/data/2.5/weather' +
                  '?zip=' + ZIPCODE + ',us' +
                  '&appid=' + APIKEY +
                  '&units=' + UNITS
                  )
    JSONWEATHER = json.loads(URL.read())
    TEMP = JSONWEATHER['main']['temp']
    print(str(int(round(TEMP, 0))) + '° ')
except:
    print('--°')
    exit()
