from django.test import TestCase
import json
import requests
url = 'http://127.0.0.1:8000/api/v1/db/list_instructors/'
headers = {'Authorization': 'Token 48b0a8a8f5b7c856fecfba91e97b21429ed45948'}
# r = requests.get(url, headers=headers)

def pprint(json_text):
    print(json.dumps(json_text, indent=2))

url_add = 'http://127.0.0.1:8000/api/v1/db/add_students/'
data =  [{ "first_name": "Shivam", "last_name": "Prasad", "email_address": "2017csb1110@iitrpr.ac.in", "entry_number": "2017csb1110"}]
# print(data)
# r = requests.post(url_add, json=data, headers=headers)
# pprint(r.json())

url_login = 'http://127.0.0.1:8000/api/v1/db/login/'
data = {"username": "amritpal@gmail.com", "password": "amritpal"}
print(data)
r = requests.post(url_login, json=data)
pprint(r.json())

url_login = 'http://127.0.0.1:8000/api/v1/db/login/'
data = {"username": "2017csb1110@iitrpr.ac.in", "password": "new_pass_123"}
print(data)
r = requests.post(url_login, json=data)
pprint(r.json())



url_assign_Instructor_to_user = 'http://127.0.0.1:8000/api/v1/db/assign_instructor_to_user/'
data = [{"email_address": "2017csb1110@iitrpr.ac.in", "instructor_id": "in002"}]
# print(data)
# r = requests.post(url_assign_Instructor_to_user, json=data, headers=headers)
# pprint(r.json())


