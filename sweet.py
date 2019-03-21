from socket import *
import requests

url = "http://206.189.42.213:8888"
# headers = {
#     "Host": "http://206.189.42.213:8888",
#     "Content-Type": "application/x-www-form-urlencoded"
# }
form_data = {"email": "sample", "username": "sample", "password": "5e8ff9bf55ba3508199d22e984129be6"}
r = requests.post("http://206.189.42.213:8888/post", data=form_data)
print(r.status_code)
