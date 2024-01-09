import requests
import json
import urllib3
from config import restCredencial as RC

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

"""Conecta unicamente con el servidor API-Rest"""
class restConector:
    """ Realiza el login al servidor para obtener el token """
    def logger(self, url, AuthorizedClient, ClientKey, ApiKey, ApiSecret):
                
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
        response_dic = json.loads(response.text)   
        
        return response_dic['creationDate'], response_dic['expirationDate'], response_dic['accessToken'], response_dic['refreshToken'], response_dic['expires']


            
    """Vamos a iniciar el Refresh Token"""

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
        response_dic = json.loads(response.text)    
        return response_dic['creationDate'], response_dic['expirationDate'], response_dic['accessToken'], response_dic['refreshToken'], response_dic['expires']
    

if __name__== "__main__":
    
    print('*********Login exitoso *********')
    #Para probar el funcionamiento el logger().
    rest_conector= restConector()
    login= rest_conector.logger(RC.LOGIN_REST_URL, RC.AUTHORIZED_CLIENT, RC.CLIENT_KEY, RC.API_KEY, RC.API_SECRET)
    
    #print('Creation Date: ' + login[0])
    #print('Expiration Date: ' + login[1])
    print("Token: " + login[2])
    print("Refres Token: " + login[3])
    #print('Expires: ' + str(login[4]))
    # Para probar que el refreshToken funcione

"""
    print('*********Refresh Token *********')

    login2= login[2]
    login3= login[3]
    refreshToken= rest_conector.refreshToken(RC.REFRESH_TOKEN_URL, login3, RC.AUTHORIZED_CLIENT, RC.CLIENT_KEY, login2 )
    print('_Creation Date: ' + refreshToken[0])
    print('_Expiration Date: ' + refreshToken[1])
    print("_Token: " + refreshToken[2])
    print("_Refres Token: " + refreshToken[3])
    print('_Expires: ' + str(refreshToken[4]))
    """