import os
import json
import requests

from settings import BASE_DIR

def get_warther():
    api_endpoint = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric"

    data_file = os.path.join(BASE_DIR, 'data', 'cities.json')
    weather_map = {}
    with open(data_file, 'r') as f:
        data_json = json.loads(f.read().encode('utf-8'))
        for item in data_json['results']:
            response = requests.get(api_endpoint.format(item))
            try:
                print item, response.json()['main']['temp']
                weather_map[item] = response.json()['main']['temp']
            except KeyError:
                print item, response.text

    save_to = os.path.join(BASE_DIR, 'data', 'weather.json')
    with open(save_to, 'w') as f:
        data = json.dumps(weather_map, sort_keys=True, indent=4, separators=(',', ': '))
        f.write(data)


if __name__ == '__main__':
    get_warther()
