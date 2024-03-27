import requests
import json
import urllib3
import sys
sys.path.append('C:/Users/Fabian/Documents/PPi_assistanst')
from SRC.config import restCredencial as RC 

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
    'Authorization': "bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJQUEF1dGguQ2xhaW1zLkdlbmVyYWwuR3JhbnRUeXBlIjpbIkRBVE9TX1BFUlNPTkFMRVMiLCJFU0NSSVRVUkEiLCJMRUNUVVJBIl0sInJvbGUiOiJQUEF1dGguUm9sLkdlbmVyYWwuVXNlclRyYWRpbmciLCJQUEF1dGguQ2xhaW1zLkdlbmVyYWwuQ3VlbnRhcyI6IjE1NzU3IiwidW5pcXVlX25hbWUiOiJ1c3VhcmlvNDE3NjYiLCJuYW1laWQiOiI0MTc2NiIsIlBQQXV0aC5DbGFpbXMuR2VuZXJhbC5GaXNydE5hbWUiOiJOb21icmUgNDE3NjYiLCJQUEF1dGguQ2xhaW1zLkdlbmVyYWwuTGFzdE5hbWUiOiJBcGVsbGlkbyA0MTc2NiIsImVtYWlsIjoibWFpbDQxNzY2QHRlc3QuY29tIiwiUFBBdXRoLkNsYWltcy5HZW5lcmFsLkV4cGlyYXRpb25UaW1lIjoiMjAyNC8wMy8yNSAxOTo0MDowOCIsIlBQQXV0aC5DbGFpbXMuR2VuZXJhbC5DbGllbnRJRCI6IkFQSV9DTElfUkVTVCIsImlzcyI6IlBQQXV0aC5zYW5kYm94LlBQSSIsImF1ZCI6Imh0dHBzOi8vYXBpX3NhbmRib3gucG9ydGZvbGlvcGVyc29uYWwuY29tIiwiZXhwIjoxNzExNDA2NDA4LCJuYmYiOjE3MTE0MDEwMDh9.9S0pm7S8tUJZWsD3uzrTJ55LmUhWXY3Q7VJpv-Cxq7Y"
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