import requests

form_data2 = {'username': 'Masha', 'password' : '12345678!'}

url2 = 'http://127.0.0.1:8000/get_form/'
r2 = requests.post(url2, data=form_data2)
print(r2.status_code, r2.text)
