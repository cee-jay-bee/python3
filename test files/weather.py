import requests

city = 'Houston'
url = 'http://api.weatherapi.com/v1/current.json?key=70e27adc27aa41afa2c25823241704&q='+city+'&aqi=no'
response = requests.get(url)
weather_json = response.json()

temp = weather_json.get('current').get('temp_f')
description = weather_json.get('current').get('condition').get('text')

print('Todays weather in', city, 'is', description, 'and', temp, 'degrees.')