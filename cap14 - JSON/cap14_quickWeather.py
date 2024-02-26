#!/home/pdajgs/python_labs/py3.7/bin/python3

import json, requests, sys, pprint

if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()

location = ''.join(sys.argv[1:]) # convertendo uma lista para uma string

url = 'http://api.openweathermap.org/data/2.5/forecast?q=%s&cnt=3&appid=fd45de6809aa9f9891717cbd0c482616' %(location)

response = requests.get(url)
response.raise_for_status()
 
# carregando dados em JSON
weatherData = json.loads(response.text)

# descrições da previsão do tempo
w = weatherData['list']

print('Current weather in %s' %(location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])