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
  "Number": "MSIG-test-CARLOS-1",
  "RequestedDeviceType": "Virtual",
  "DeliveryMethod": "ByHand",
  "Customer": {
    "Name": "CARLOS",
    "Number": "111"
  },
  "Vehicle": {
    "VIN": "VINMSI11G001",
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



response = requests.request("POST", url, headers=headers, data=payload)
print(response.reason)
print(response.elapsed.total_seconds())


    