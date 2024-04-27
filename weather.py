import os
import requests
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()

API_KEY = os.getenv('API_KEY')

@dataclass
class weather_data():
  main: str
  description: str
  icon: str
  temperature: float

def get_latitude_longitude(city_name, state_code, country_code, API_key):
  r = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}').json()
  lat, lon = r[0].get('lat', None), r[0].get('lon', None)
  return lat, lon

def get_weather(lat, lon, API_KEY):
  r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric').json()
  data = weather_data(
    main = r.get('weather')[0].get('main'),
    description = r.get('weather')[0].get('description'),
    icon = r.get('weather')[0].get('icon'),
    temperature=r.get('main').get('temp')
  )
  
  return data
  
def main(city_name, state_code, country_code):
  lat, lon = get_latitude_longitude(city_name, state_code, country_code, API_KEY)
  weather_data = get_weather(lat, lon, API_KEY)
  return weather_data
  
if __name__ == '__main__':
  lat, lon = get_latitude_longitude('Toronto', 'ON', 'CA', API_KEY)
  get_weather(lat, lon, API_KEY)
