import requests
from requests.exceptions import RequestException
import os
import sys

def main():
  api_endpoint = 'https://api.openweathermap.org/data/2.5/weather'
  lat = os.getenv('LAT')
  lon = os.getenv('LON')
  api_key = os.getenv('API_KEY')
  try:
    params = {'lat': lat,
              'lon': lon,
              'appid': api_key}
    response = requests.get(url=api_endpoint, params=params)
    data = response.json()
    print(data)
  except RequestException as exception:
    print(exception)
    sys.exit()

if __name__ == '__main__':
  main()