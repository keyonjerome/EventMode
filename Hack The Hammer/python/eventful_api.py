import json
import requests

url = 'http://api.eventful.com/json/events/search'

params = {
    'keywords': 'technology',
    'location': 'Ontario',
    'app_key': 'VhJWmCTVhqLHmrGT',
    'page_size': 10000
}

r = requests.get(url=url, params=params)

json_file = open('eventful_technology.json', 'w', encoding='utf-8')
json_file.write(r.text)
json_file.close()
