import requests
import json

url = "https://poc.connectedcar360.net/V1/token"

payload='grant_type=password&username=Admin&password=sCCbj!23'
headers = {
  'Authorization': 'Basic YWRtaW46IVFBWjJ3c3g=',
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)
response_dict = response.json()
print(response_dict['access_token'])