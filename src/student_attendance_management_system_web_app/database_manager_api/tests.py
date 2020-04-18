from django.test import TestCase
import json
import requests
from django.http import JsonResponse


def json_extractor(data_json, field):
    json_str = json.dumps(data_json)
    data_loads = json.loads(json_str)
    return data_loads[field]


def pprint(json_text):
    print(json.dumps(json_text, indent=2))

print("""       

      **  LOGGING IN  **      
        
""")

# url_login = 'http://127.0.0.1:8000/api/v1/db/login/'
# data = {"username": "2017csb1110@iitrpr.ac.in", "password": "new_pass_123"}

url_login = 'http://127.0.0.1:8000/api/v1/db/login/'
data = {"username": "amritpal@gmail.com", "password": "new_pass_123"}
# print(data)
r = requests.post(url_login, json=data)
pprint(r.json())
print('status code is ', r.status_code)
token = ''
if(r.status_code == 200):
    token = json_extractor(r.json(), 'token')
headers = {'Authorization': f'Token {token}'}



print("""       

      **  Getting User Info  **      
        
""")
url_user_info = 'http://127.0.0.1:8000/api/v1/db/get_user_info/'
data = {"email": "amritpal@gmail.com", "password": "new_pass_123"}
r = requests.get(url_user_info,data=data, headers=headers)
print(r.status_code)
pprint(r.json())



print("""       

      **  LISTING ALL STUDENTS  **
        
""")
url_list_student = 'http://127.0.0.1:8000/api/v1/db/list_students/'
r = requests.get(url_list_student, headers=headers)
pprint(r.json())



print("""       

      **  ADDING NEW STUDENTS  **
        
""")
url_add = 'http://127.0.0.1:8000/api/v1/db/add_students/'
data =  [{ "first_name": "Amritpal", "last_name": "Singh", "email": "2017csb1068@iitrpr.ac.in", "entry_number": "2017csb1068"},
        { "first_name": "Ankit", "last_name": "Something", "email": "2017csb1069@iitrpr.ac.in", "entry_number": "2017csb1069"} ]
# pprint(data)
r = requests.post(url_add, json=data, headers=headers)
pprint(r.json())
print('status code is ', r.status_code)


print("""       

      **  LISTING ALL INSTRUCTORS  **
        
""")
url_instructors = 'http://127.0.0.1:8000/api/v1/db/list_instructors/'
r = requests.get(url_instructors, headers=headers)
pprint(r.json())
print('status code is ', r.status_code)




print("""       

      **  ASSIGN  INSTRUCTOR TO USER  **
        
""")
url_assign_Instructor_to_user = 'http://127.0.0.1:8000/api/v1/db/assign_instructor_to_user/'
data = [{"email": "2017csb1110@iitrpr.ac.in", "instructor_id": "in002"}]
# print(data)
r = requests.post(url_assign_Instructor_to_user, json=data, headers=headers)
pprint(r.json())
print('status code is ', r.status_code)




print("""       

      **  ADD NEW COURSE  **
        
""")
url_add_course = 'http://127.0.0.1:8000/api/v1/db/add_courses/'
data = [{
    "name": "Networking",
    "code": "cs304",
    "instructor_ids": ["in001", "in0069"],
    "teaching_assistant_ids": ["1"],
    "student_ids": ["2017csb1068", "2017csb1069"],
    "relative_attendance_for_one_lecture": 1,
    "relative_attendance_for_one_tutorial": 1,
    "relative_attendance_for_one_practical": 1
    }]
# print(data)
r = requests.post(url_add_course, json=data, headers=headers)
pprint(r.json())
print('status code is ', r.status_code)

