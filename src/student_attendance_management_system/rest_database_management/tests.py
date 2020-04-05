from django.test import TestCase
import json
import requests
url = 'http://127.0.0.1:8000/api/v1/db/list_instructors/'
headers = {'Authorization': 'Token 48b0a8a8f5b7c856fecfba91e97b21429ed45948'}
# r = requests.get(url, headers=headers)

url_add = 'http://127.0.0.1:8000/api/v1/db/add_students/'
data =  [{ "first_name": "Shivam", "last_name": "Prasad", "email_address": "2017csb1110@iitrpr.ac.in", "entry_number": "2017csb1101"}]
print(json.dumps(data))
r = requests.post(url_add, json=data, headers=headers)
print(r.json())

