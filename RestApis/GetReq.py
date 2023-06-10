import json
import requests
from jsonpath_ng import jsonpath
from jsonpath_ng.ext import parse


req = requests.get("http://webservice.toscacloud.com/rest/api/Employee_V2",headers={'Authorization':'Bearer cdcca385-a65e-4068-8272-7c937dcc57bb'})
print(req.status_code)
json_data = req.json()
print(json.dumps(json_data,indent=4))

json_Exp = parse('$[?(@.FirstName == "venkat")].Address')

address = json_Exp.find(json_data)
#print(address)
print(address[0])
print(address[0].value['City'])