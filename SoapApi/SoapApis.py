import requests

url = 'https://tosca-webservice.azurewebsites.net/Calculator.svc/ssl'

xmldata = '''
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:cal="http://CalculatorService">
   <soapenv:Header/>
   <soapenv:Body>
      <cal:Add>
         <!--Optional:-->
         <cal:n1>5</cal:n1>
         <!--Optional:-->
         <cal:n2>10</cal:n2>
      </cal:Add>
   </soapenv:Body>
</soapenv:Envelope>
'''

headers = {
"Content-Type": "text/xml",
"SOAPAction": "http://CalculatorService/ICalculator/Add"
}

response = requests.post(url=url, data=xmldata,headers=headers)
print(response.status_code)
print(response.text)
