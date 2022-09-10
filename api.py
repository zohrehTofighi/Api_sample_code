import datetime as dt
from tkinter.filedialog import Open
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('api_key.txt', 'r').read()
CITY = "London"

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()

print(response)
print(100*'*')
print(url)
print(100*'*')
for keys, values in response.items():
    print(keys)
    print(values)
    


