from conector import restConector
from config import restCredencial as RC
from dateutil import parser
from datetime import  datetime
import json


""" stores, updates, and provides access to API authorization data, stored in an environment variable"""
class tokenManager:

    def exporter(self, jsonFilePath, inicialTimeStr, expTimeStr, token, bearerToken,refreshToken, expires):

        self.jsonFilePath= jsonFilePath
        self.inicialTimeStr= inicialTimeStr
        self.expTimeStr= expTimeStr
        self.token= token
        self.bearerToken= bearerToken
        self.refreshToken= refreshToken
        self.expires= expires
        
        data_dict= {"cretionTime":str(self.inicialTimeStr),
                    "expirationTime":str(self.expTimeStr),
                    "token":str(self.token),
                    "bearerToken":str(self.bearerToken),
                    "refreshToken":str(self.refreshToken),
                    "expires":str(self.expires)
                    }       
 
        with open(self.jsonFilePath, 'w', encoding = 'utf-8') as json_file:
            jsonString = json.dumps(data_dict, indent= 4)
            json_file.write(jsonString)
            

    def importer(self, jsonFilePath):

        self.jsonFilePath= jsonFilePath


        with open(self.jsonFilePath, "r", encoding = 'utf-8') as json_file:
            data= json.load(json_file)
            
            token= data['token']
            bearerToken= data['bearerToken']
            refreshToken= data['refreshToken']
            expires= data['expires']
            
            creationDate= data['cretionTime']
            inicialTime= parser.parse(creationDate)
            inicialTimeStr=inicialTime.strftime('%Y-%m-%d %H:%M:%S')
            creationTime= datetime.strptime(inicialTimeStr, '%Y-%m-%d %H:%M:%S')

            expirationDate= data['expirationTime']
            expTime= parser.parse(expirationDate)
            expTimeStr= expTime.strftime('%Y-%m-%d %H:%M:%S')
            expirationTime=datetime.strptime(expTimeStr, '%Y-%m-%d %H:%M:%S')

        return creationTime, expirationTime, token, bearerToken, refreshToken, expires
    




if __name__== "__main__":

    #Conexion a la API
    #rest_conector= restConector()
    #login= rest_conector.conector(RC.LOGIN_REST_URL, RC.AUTHORIZED_CLIENT, RC.CLIENT_KEY, RC.API_KEY, RC.API_SECRET)
    #token=login[2]
    #bearerToken= login[3]
    #refreshToken= login[4]
    #expires= login[5]

    #Convertir formato de fecha str-->datetime
    #creationDate= login[0]
    #inicialTime= parser.parse(creationDate)
    #inicialTimeStr=inicialTime.strftime('%Y-%m-%d %H:%M:%S')
    #cretionTime= datetime.strptime(inicialTimeStr, '%Y-%m-%d %H:%M:%S')
    #expirationDate= login[1]
    #expTime= parser.parse(expirationDate)
    #expTimeStr= expTime.strftime('%Y-%m-%d %H:%M:%S')
    #expirationTime=datetime.strptime(expTimeStr, '%Y-%m-%d %H:%M:%S')

    #print(type(inicialTimeStr))
    #print(type(expTimeStr))
    #print(type(token))
    #print(type(bearerToken))
    #print(type(refreshToken))
    #print(type(expires))

    credenciales= tokenManager()
    jsonFilePath= r'data.json'

    #exportar= credenciales.exporter(jsonFilePath, inicialTimeStr, expTimeStr, token, bearerToken, refreshToken, expires)

    #importar= credenciales.importer(jsonFilePath)

    #print(importar[0])
    #print(type(importar[0]))
    #print(type(expTimeStr))
    #print(type(token))
    #print(type(bearerToken))
    #print(type(refreshToken))
    #print(type(expires))
