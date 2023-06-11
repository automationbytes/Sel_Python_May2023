import requests

url = 'https://tosca-webservice.azurewebsites.net/TempConvert.svc/ssl'

xmldata = '''
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://www.w3schools.com/webservices/">
   <soapenv:Header/>
   <soapenv:Body>
      <web:CelsiusToFahrenheit>
         <!--Optional:-->
         <web:Celsius>40</web:Celsius>
      </web:CelsiusToFahrenheit>
   </soapenv:Body>
</soapenv:Envelope>
'''

headers = {
"Content-Type": "text/xml",
"SOAPAction": "http://www.w3schools.com/webservices/CelsiusToFahrenheit"
}

response = requests.post(url=url, data=xmldata,headers=headers)
print(response.status_code)
print(response.text)
