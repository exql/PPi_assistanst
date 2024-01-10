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
  'AuthorizedClient': 'API_CLI_REST',
  'ClientKey': 'ppApiCliSB',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJQUEF1dGguQ2xhaW1zLkdlbmVyYWwuR3JhbnRUeXBlIjpbIkRBVE9TX1BFUlNPTkFMRVMiLCJFU0NSSVRVUkEiLCJMRUNUVVJBIl0sInJvbGUiOiJQUEF1dGguUm9sLkdlbmVyYWwuVXNlclRyYWRpbmciLCJQUEF1dGguQ2xhaW1zLkdlbmVyYWwuQ3VlbnRhcyI6IjE1NzU3IiwidW5pcXVlX25hbWUiOiJ1c3VhcmlvNDE3NjYiLCJuYW1laWQiOiI0MTc2NiIsIlBQQXV0aC5DbGFpbXMuR2VuZXJhbC5GaXNydE5hbWUiOiJOb21icmUgNDE3NjYiLCJQUEF1dGguQ2xhaW1zLkdlbmVyYWwuTGFzdE5hbWUiOiJBcGVsbGlkbyA0MTc2NiIsImVtYWlsIjoibWFpbDQxNzY2QHRlc3QuY29tIiwiUFBBdXRoLkNsYWltcy5HZW5lcmFsLkV4cGlyYXRpb25UaW1lIjoiMjAyNC8wMS8wOSAxNjowNjo1MiIsIlBQQXV0aC5DbGFpbXMuR2VuZXJhbC5DbGllbnRJRCI6IkFQSV9DTElfUkVTVCIsImlzcyI6IlBQQXV0aC5zYW5kYm94LlBQSSIsImF1ZCI6Imh0dHBzOi8vYXBpX3NhbmRib3gucG9ydGZvbGlvcGVyc29uYWwuY29tIiwiZXhwIjoxNzA0ODI3MjEyLCJuYmYiOjE3MDQ4MjE4MTJ9.HydEOqJpT4BN7zpei5Nb_3qet09ap952t70V3Q0tr8k'
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response.text)