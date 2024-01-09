import requests
import json
import urllib3
import sys
sys.path.append('C:/Users/Fabian/Documents/PPi_assistanst/SRC')
from config import restCredencial as RC 

""" Retrieves all the available accounts and their officer for the current session.
"""    
url = RC.ACCOUNT_URL
#'https://clientapi_sandbox.portfoliopersonal.com/api/1.0/Account/Accounts'
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

payload = {}
headers = {
    'AuthorizedClient': RC.AUTHORIZED_CLIENT,
    'ClientKey': RC.CLIENT_KEY,
    'Content-Type': 'application/json',
    'Authorization': 'Bearer '
    }

response = requests.request("GET", url, headers=headers, data=payload, verify=False)
if response.ok:
    response_dic= json.loads(response.text)
    accountNumber= response_dic[0]['accountNumber']
    cuenta= response_dic[0]['name']

    print(response_dic)
    print('Account Number: ')
    print(accountNumber)
    print('Cuenta: ')
    print(cuenta)
else:
    print(response)