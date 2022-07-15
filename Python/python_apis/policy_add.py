import requests
import json
from requests.structures import CaseInsensitiveDict


url = "https://msigretail.connectedcar360.net/V1/token"

payload='grant_type=password&username=Admin&password=sCCbj!23'
headers = {
  'Authorization': 'Basic YWRtaW46IVFBWjJ3c3g=',
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

response_dict = response.json()
access_token = (response_dict['access_token'])


url = "https://msigretail.connectedcar360.net/v1/api/policies/add"

payload = json.dumps({
  "Number": "MSIG-RETAIL-CARLOS",
  "RequestedDeviceType": "Virtual",
  "DeliveryMethod": "ByHand",
  "Customer": {
    "Name": "CARLOS",
    "Number": "938"
  },
  "Vehicle": {
    "VIN": "VINMSIG001",
    "LicensePlate": "8552111",
    "Make": "TOYOTA",
    "Model": "TOYOTA HILUX L",
    "YearOfInitialRegistration": 2017,
    "MotorType": "Diesel"
  }
})

headers = CaseInsensitiveDict()

headers = {'Authorization': 'Bearer ' + access_token}
headers["Content-Type"] = "application/json"

# headers = {
#   'Authorization': 'Bearer tm6T7sUNYb5Kb-D4ujpUTQZ2pOVhyg_WOxOYav5bBOj3s7GqIJv2lNpfQ7NTWmVn17Lfqq82jN6AvFr3qVUgjKWGWj-H2aoROHmVow2KVo2k1nxcZQomsixwV7oyfedenBhQoWpH9PEUM4koy3iXvZEtg93gx5I5i4wzDP36mRKJ5AYTVwVRFmHl2yrg7R4qjBFu6Bn2jYtH39aCTxJxYCJHLu_gQ9QW1tGSgHBSwyuM0o2ApqqArwTeFnc4AYkoWoRJ8D2F4th6YyDIpwjOmbMJFP27tct4JeesT6UX7HH56M8XG2n8SAfxFmXLyYgoI6_cAniWOT3O2c7m_l1R5TcwiTi6443JZCU4B6vuZbFNtmvC51SUVDM_NDUkZMbJVytiKZm9oM7vZpaj2ZRMIbrJHStHdNLtcazzFUzsRHvagZMJ92ErhF5O5kvYa9It6InKjwZXI9UaE3RxPXK_DkoW5xBBUygVKwEhSYBvapre49406pxVvwb4VmzMHTtBqOh4oI5BdH-3t-2YvYGCiA',
#   
#   'Content-Type': 'application/json'
# }

response = requests.request("POST", url, headers=headers, data=payload)
print(response.reason)
print(response.elapsed.total_seconds())

# print(access_token)
    