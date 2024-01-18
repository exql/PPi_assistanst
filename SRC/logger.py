from conector import restConector
from config import restCredencial as RC
from dateutil import parser
from datetime import  datetime
import json

class credencial:

    def exporter(self, inicialTimeStr, expTimeStr, token, bearerToken,refreshToken, expires ):

        #self.jsonFilePath= jsonFilePath,
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
 
        with open(r'data.json', 'w', encoding = 'utf-8') as json_file:
            jsonString = json.dumps(data_dict, indent= 4)
            json_file.write(jsonString)
        
        print("bien")


if __name__== "__main__":

    rest_conector= restConector()
    login= rest_conector.conector(RC.LOGIN_REST_URL, RC.AUTHORIZED_CLIENT, RC.CLIENT_KEY, RC.API_KEY, RC.API_SECRET)

    creationDate= login[0]
    inicialTime= parser.parse(creationDate)
    inicialTimeStr=inicialTime.strftime('%Y-%m-%d %H:%M:%S')
    cretionTime= datetime.strptime(inicialTimeStr, '%Y-%m-%d %H:%M:%S')

    expirationDate= login[1]
    expTime= parser.parse(expirationDate)
    expTimeStr= expTime.strftime('%Y-%m-%d %H:%M:%S')
    expirationTime=datetime.strptime(expTimeStr, '%Y-%m-%d %H:%M:%S')

    token=login[2]
    bearerToken= login[3]
    refreshToken= login[4]
    expires= login[5]

    """def token_json(jsonFilePath):
        data_dict= {"cretionTime":inicialTimeStr,
                    "expirationTime":expTimeStr,
                    "token":token,
                    "bearerToken":bearerToken,
                    "refreshToken":refreshToken,
                    "expires":expires
                    }       
 
        with open (jsonFilePath, 'w', encoding = 'utf-8') as json_file:
            jsonString = json.dumps(data_dict, indent= 4)
            json_file.write(jsonString)    """
   
    print(type(inicialTimeStr))
    print(type(expTimeStr))
    print(type(token))
    print(type(bearerToken))
    print(type(refreshToken))
    print(type(expires))

credenciales= credencial()

exportar= credenciales.exporter(inicialTimeStr, expTimeStr, token, bearerToken, refreshToken, expires)

#Estaría bueno agregar el modulo de pasar las fechas de STR a datetime 
#y creación del json a los metodos conector y refresh token
#Pero con la diferencía en el refresh token que tomen los datos desde el json.

