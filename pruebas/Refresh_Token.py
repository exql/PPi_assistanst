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
  'Authorization': ''
  }
response = requests.request("POST", url, headers=headers, data=payload, verify=False)
response_dic = json.loads(response.text)
    
print (response_dic['creationDate']) 
print (response_dic['expirationDate'])
print (response_dic['accessToken'])
print (response_dic['refreshToken'])
print (response_dic['expires'])

