import requests
import json
import urllib3
from config import restCredencial as RC

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

"""Conecta unicamente con el servidor API-Rest"""
class restConector:
    """ Realiza el login al servidor para obtener el token """
    def conector(self, url, AuthorizedClient, ClientKey, ApiKey, ApiSecret):
                
        self.url=url
        self.AuthorizedClient= AuthorizedClient
        self.ClientKey= ClientKey
        self.ApiKey= ApiKey
        self.ApiSecret= ApiSecret     

        payload = ""
        headers = {
            'AuthorizedClient': self.AuthorizedClient,
            'ClientKey': self.ClientKey,
            'Content-Type': 'application/json',
            'ApiKey': self.ApiKey,
            'ApiSecret': self.ApiSecret
            }
        response = requests.request("POST", url, headers=headers, data=payload, verify=False)
        
        if response.ok:
            print('********* Login exitoso *********')
            response_dic = json.loads(response.text)
            token= response_dic['accessToken']
            bearer= response_dic['tokenType']
            bearerToken= bearer+ ' ' + token

            return response_dic['creationDate'], response_dic['expirationDate'], token, bearerToken, response_dic['refreshToken'], response_dic['expires']
        else:
            print("********* Error de conexion " + str(response.status_code) + " *********")
        

          
    """Realiza la renovación del token"""

    def refreshToken(self,url, rfToken, AuthorizedClient, ClientKey, accessToken  ):

        self.url=url
        self.rfToken= rfToken
        self.AuthorizedClient= AuthorizedClient
        self.ClientKey= ClientKey
        self.accessToken= accessToken     

        payload =  json.dumps({
        "refreshToken": self.rfToken
        })

        headers = {
        'AuthorizedClient': self.AuthorizedClient,
        'ClientKey': self.ClientKey,
        'Content-Type': 'application/json',        
        'Authorization': self.accessToken
        }

        response = requests.request("POST", url, headers=headers, data=payload, verify=False)
        if response.ok:
            print('********* Reconexión exitosa *********')
            response_dic = json.loads(response.text)
            token= response_dic['accessToken']
            bearer= response_dic['tokenType']
            bearerToken= bearer+ ' ' + token
            return response_dic['creationDate'], response_dic['expirationDate'], token, bearerToken, response_dic['refreshToken'], response_dic['expires']
        else:
            print("********* Error de conexion " + str(response.status_code) + " *********")

if __name__== "__main__":
    #Para probar el funcionamiento el conector().
    rest_conector= restConector()
    login= rest_conector.conector(RC.LOGIN_REST_URL, RC.AUTHORIZED_CLIENT, RC.CLIENT_KEY, RC.API_KEY, RC.API_SECRET)
   
    #print('Creation Date: ' + login[0])
    #print('Expiration Date: ' + login[1])
    #print("Token: " + login[2])
    #print("Bearer Token: " + login{3})
    #print("Refres Token: " + login[4])
    #print('Expires: ' + str(login[5]))
    # Para probar que el refreshToken funcione


    print('********* Probando Refresh Token *********')

    token= login[2]
    refreshToken= login[4]
    refreshToken= rest_conector.refreshToken(RC.REFRESH_TOKEN_URL, refreshToken, RC.AUTHORIZED_CLIENT, RC.CLIENT_KEY, token )
    print('_Creation Date: ' + refreshToken[0])
    print('_Expiration Date: ' + refreshToken[1])
    print("_Token: " + refreshToken[2])
    print("_Bearer Token: " + refreshToken[3])
    print("_Refres Token: " + refreshToken[4])
    print('_Expires: ' + str(refreshToken[5]))
    