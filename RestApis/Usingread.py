import json
import requests
from jsonpath_ng import jsonpath
from jsonpath_ng.ext import parse

with open('input.json','r') as file:
    myjson = file.read()

req = requests.post("http://tosca-webservice-ng.azurewebsites.net/api/Shops_V4",json = myjson, headers = {'Authorization':'Bearer cdcca385-a65e-4068-8272-7c937dcc57bb'})
print(req.status_code)

print(json.dumps(req.json(),indent=4))

getreq = requests.get("http://tosca-webservice-ng.azurewebsites.net/api/Shops_V4")
print(getreq.status_code)

print(json.dumps(getreq.json(),indent=4))
