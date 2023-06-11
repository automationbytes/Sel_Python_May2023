from zeep import Client
from zeep.transports import Transport
from zeep.plugins import HistoryPlugin
#
history = HistoryPlugin()
wsdl_link = "http://webservice.toscacloud.com/Calculator.svc?singleWsdl"
client = Client(wsdl=wsdl_link,transport=Transport(timeout=100),plugins=[history])
response = client.service.Add(n1=5,n2=10)
print(response)
print(history.last_received)
print(history.last_sent)
#
#
# client = Client("http://webservice.toscacloud.com/Calculator.svc?singleWsdl")
# with client.settings(raw_response=True):
#     response = client.service.Add(n1=5,n2=10)
#     print(response.status_code)
#     print(response.content)
