# Dinero disponible en la cuenta para poder utilizar.

import requests
import json
import urllib3
import sys
sys.path.append('C:/Users/Fabian/Documents/PPi_assistanst/SRC')
from config import restCredencial as RC 

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


url= "https://clientapi_sandbox.portfoliopersonal.com/api/1.0/Account/AvailableBalance?accountNumber=150100"


payload = {}
headers = {
  'AuthorizedClient': RC.AUTHORIZED_CLIENT,
  'ClientKey': RC.CLIENT_KEY,
  'Content-Type': 'application/json',
  'Authorization': 'Bearer '
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response.text)

