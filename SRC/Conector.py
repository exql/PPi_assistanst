import requests
import json
import urllib3
from dateutil import parser
from datetime import  datetime
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

            creationDate= response_dic['creationDate']
            inicialTime= parser.parse(creationDate)
            inicialTimeStr=inicialTime.strftime('%Y-%m-%d %H:%M:%S')
            #creationTime= datetime.strptime(inicialTimeStr, '%Y-%m-%d %H:%M:%S')

            expirationDate= response_dic['expirationDate']
            expTime= parser.parse(expirationDate)
            expTimeStr= expTime.strftime('%Y-%m-%d %H:%M:%S')
            #expirationTime=datetime.strptime(expTimeStr, '%Y-%m-%d %H:%M:%S')

            refreshToken= response_dic['refreshToken']
            expires= response_dic['expires']
        
            data_dict= {"cretionTime":inicialTimeStr,
                        "expirationTime":expTimeStr,
                        "token":token,
                        "bearerToken":bearerToken,
                        "refreshToken":refreshToken,
                        "expires":expires
                        }

            jsonFilePath= r'data.json'      
        
            with open (jsonFilePath, 'w', encoding = 'utf-8') as json_file:
                jsonString = json.dumps(data_dict, indent= 4)
                json_file.write(jsonString)  
            
            return response_dic['creationDate'], response_dic['expirationDate'], token, bearerToken, response_dic['refreshToken'], response_dic['expires']
        else:
            print("********* Error de conexion " + str(response.status_code) + " *********")
        

          
    """Realiza la renovación del token"""

    def refreshToken(self, jsonFilePath, url, AuthorizedClient, ClientKey):

        self.jsonFilePath= jsonFilePath
        self.url=url
        #self.rfToken= rfToken --> agregar el argumento
        self.AuthorizedClient= AuthorizedClient
        self.ClientKey= ClientKey
        #self.accessToken= accessToken --> agregar el argumento  
                
        with open(self.jsonFilePath, "r", encoding = 'utf-8') as json_file:
            data= json.load(json_file)
            token= data['token']
            refreshToken= data['refreshToken']
            
        payload =  json.dumps({
        "refreshToken": refreshToken
        })

        headers = {
        'AuthorizedClient': self.AuthorizedClient,
        'ClientKey': self.ClientKey,
        'Content-Type': 'application/json',        
        'Authorization': token
        }

        response = requests.request("POST", url, headers=headers, data=payload, verify=False)
        if response.ok:
            print('********* Reconexión exitosa *********')
            response_dic = json.loads(response.text)
            token= response_dic['accessToken']
            bearer= response_dic['tokenType']
            bearerToken= bearer+ ' ' + token

            creationDate= response_dic['creationDate']
            inicialTime= parser.parse(creationDate)
            inicialTimeStr=inicialTime.strftime('%Y-%m-%d %H:%M:%S')
            #creationTime= datetime.strptime(inicialTimeStr, '%Y-%m-%d %H:%M:%S')

            expirationDate= response_dic['expirationDate']
            expTime= parser.parse(expirationDate)
            expTimeStr= expTime.strftime('%Y-%m-%d %H:%M:%S')
            #expirationTime=datetime.strptime(expTimeStr, '%Y-%m-%d %H:%M:%S')

            refreshToken= response_dic['refreshToken']
            expires= response_dic['expires']
        
            data_dict= {"cretionTime":inicialTimeStr,
                        "expirationTime":expTimeStr,
                        "token":token,
                        "bearerToken":bearerToken,
                        "refreshToken":refreshToken,
                        "expires":expires
                        }

              
        
            with open (self.jsonFilePath, 'w', encoding = 'utf-8') as json_file:
                jsonString = json.dumps(data_dict, indent= 4)
                json_file.write(jsonString)  
            
            return response_dic['creationDate'], response_dic['expirationDate'], token, bearerToken, response_dic['refreshToken'], response_dic['expires']
        else:
            print("********* Error de conexion " + str(response.status_code) + " *********")

if __name__== "__main__":
    #Para probar el funcionamiento el conector().
    rest_conector= restConector()
    jsonFilePath= r'data.json'
    login= rest_conector.conector(RC.LOGIN_REST_URL, RC.AUTHORIZED_CLIENT, RC.CLIENT_KEY, RC.API_KEY, RC.API_SECRET)
   
    #print('Creation Date: ' + login[0])
    #print('Expiration Date: ' + login[1])
    #print("Token: " + login[2])
    #print("Bearer Token: " + login[3])
    #print("Refres Token: " + login[4])
    #print('Expires: ' + str(login[5]))


    #print('********* Probando Refresh Token *********')

    #refreshToken= rest_conector.refreshToken(jsonFilePath, RC.REFRESH_TOKEN_URL, RC.AUTHORIZED_CLIENT, RC.CLIENT_KEY)
    #print('_Creation Date: ' + refreshToken[0])
    #print('_Expiration Date: ' + refreshToken[1])
    #print("_Token: " + refreshToken[2])
    #print("_Bearer Token: " + refreshToken[3])
    #print("_Refres Token: " + refreshToken[4])
    #print('_Expires: ' + str(refreshToken[5]))
    