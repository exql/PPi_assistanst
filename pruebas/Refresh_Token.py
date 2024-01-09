import requests
import json
from SRC.config import restCredencial as RC

url = RC.REFRESH_TOKEN_URL
#"https://clientapi_sandbox.portfoliopersonal.com/api/1.0/Account/RefreshToken"

payload = json.dumps({
     "refreshToken": '09c396a21fc8498fb128320ef8c557a5'
})
headers = {
  'AuthorizedClient': RC.AUTHORIZED_CLIENT,
  'ClientKey': RC.CLIENT_KEY,
  'Content-Type': 'application/json',
  # Se pone el "accessToken" generado en el login
  'Authorization': 'yJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJQUEF1dGguQ2xhaW1zLkdlbmVyYWwuR3JhbnRUeXBlIjpbIkRBVE9TX1BFUlNPTkFMRVMiLCJFU0NSSVRVUkEiLCJMRUNUVVJBIl0sInJvbGUiOiJQUEF1dGguUm9sLkdlbmVyYWwuVXNlclRyYWRpbmciLCJQUEF1dGguQ2xhaW1zLkdlbmVyYWwuQ3VlbnRhcyI6IjE1NzU3IiwidW5pcXVlX25hbWUiOiJ1c3VhcmlvNDE3NjYiLCJuYW1laWQiOiI0MTc2NiIsIlBQQXV0aC5DbGFpbXMuR2VuZXJhbC5GaXNydE5hbWUiOiJOb21icmUgNDE3NjYiLCJQUEF1dGguQ2xhaW1zLkdlbmVyYWwuTGFzdE5hbWUiOiJBcGVsbGlkbyA0MTc2NiIsImVtYWlsIjoibWFpbDQxNzY2QHRlc3QuY29tIiwiUFBBdXRoLkNsYWltcy5HZW5lcmFsLkNsaWVudElEIjoiQVBJX0NMSV9SRVNUIiwiUFBBdXRoLkNsYWltcy5HZW5lcmFsLkV4cGlyYXRpb25UaW1lIjoiMjAyNC8wMS8wNyAxNToyMTo1NCIsImlzcyI6IlBQQXV0aC5zYW5kYm94LlBQSSIsImF1ZCI6Imh0dHBzOi8vYXBpX3NhbmRib3gucG9ydGZvbGlvcGVyc29uYWwuY29tIiwiZXhwIjoxNzA0NjUxNzE0LCJuYmYiOjE3MDQ2NDYzMTR9.hkhfZpmp8NOmBz1c_YwdWGiazTbSAuEyIJnYTQlmoCM'
  }
response = requests.request("POST", url, headers=headers, data=payload, verify=False)
response_dic = json.loads(response.text)
    
print (response_dic['creationDate']) 
print (response_dic['expirationDate'])
print (response_dic['accessToken'])
print (response_dic['refreshToken'])
print (response_dic['expires'])

