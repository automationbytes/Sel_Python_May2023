import requests
import json
from Employee import Employee

#create obj
employee = Employee(firstname="Tom",lastname="Jerry",eid =1, city="Chennai",country="India",street="123 abc streeet", zipcode=489790)

employeereq = employee.mydict()

req = requests.put("http://tosca-webservice-ng.azurewebsites.net/api/Employee_V4",json=employeereq)
print(req.status_code)
print(req)