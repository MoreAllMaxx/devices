import requests
from devices.api.utils import get_mac_48
import random

choices = ('emeter', 'zigbee', 'lora', 'gsm', )

response_anagram = requests.post(
    'http://127.0.0.1:8000/api/devices/', data={'dev_id': get_mac_48(), 'dev_type': random.choice(choices)})
print(response_anagram.status_code)


response_not_anagram = requests.post(
    'http://127.0.0.1:8000/api/anagram/', data={'dev_id': '123', 'dev_type': '321'})
print(response_not_anagram.status_code)

response_query = requests.get('http://127.0.0.1:8000/api/devices_query/')
print(response_query.json())
