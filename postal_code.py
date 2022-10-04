import requests

import json

endpoint = "https://api.postalpincode.in/pincode/"

pincode = input("Enter Your Pincode :")

url = endpoint+pincode

response = requests.get(url)

data = json.loads(response.text)
final_data = data[0]['PostOffice']

for i in final_data:  
    print(i['Name'])
    print(i['Block'])
    print(i['District'])
    print(i['State'])
    print(i['Country'])
    print()
print()

final_data = data[0]['PostOffice'][0]
for key,value in final_data.items():
    print(f"{key} : {value}")
