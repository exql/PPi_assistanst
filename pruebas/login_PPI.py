import requests
import json
import urllib3
import sys
sys.path.append('C:/Users/Fabian/Documents/PPi_assistanst/SRC')
from config import restCredencial as RC 


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if __name__=="__main__":

  url = RC.LOGIN_REST_URL
  #'https://clientapi_sandbox.portfoliopersonal.com/api/1.0/Account/LoginApi'

  payload = ""
  headers = {
    'AuthorizedClient': RC.AUTHORIZED_CLIENT,
    'ClientKey': RC.CLIENT_KEY,
    'Content-Type': 'application/json',
    'ApiKey': RC.API_KEY,
    'ApiSecret': RC.API_SECRET
    }

  response = requests.request("POST", url, headers=headers, data=payload, verify=False)
  #print(response)
  response_dic = json.loads(response.text)
  #print(response_dic)
  access_Token = response_dic['accessToken']
  #refresh_Token = response_dic['refreshToken']
  print("Access Token: " + access_Token)
  #print("Refresh Token: " + refresh_Token)


  #print(response.text)