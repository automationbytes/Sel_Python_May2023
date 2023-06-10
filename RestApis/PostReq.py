import json
import requests
from jsonpath_ng import jsonpath
from jsonpath_ng.ext import parse

myjson = {
  "city": "Chennai",
  "country": "India",
  "name": "Dev Labs"
}

req = requests.post("http://tosca-webservice-ng.azurewebsites.net/api/Shops_V4",json = myjson)
print(req.status_code)

print(json.dumps(req.json(),indent=4))

getreq = requests.get("http://tosca-webservice-ng.azurewebsites.net/api/Shops_V4")
print(getreq.status_code)

print(json.dumps(getreq.json(),indent=4))
