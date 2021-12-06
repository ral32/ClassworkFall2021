import requests

server_name = "http://vcm-7631.vm.duke.edu:5002"

r = requests.get(server_name+"/get_patients/ral32")
print(r.text)

r = requests.get(server_name+"/get_blood_type/M1")
print(r.text)

r = requests.get(server_name+"/get_blood_type/F4")
print(r.text)

dict = {"Name": "ral32", "Match": "No"}
r = requests.post(server_name+"/match_check", json=dict)
if r.status_code != 200:
    print(r.text)
else:
    print(r.text)
