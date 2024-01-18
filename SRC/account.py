import requests
import json
import urllib3
from config import restCredencial as RC
from conector import restConector

    
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


""" Retrieves all data of the available accounts """
class accounts:

    """ Retrieves the account number """
    def accountNum(self, url, authorizedClient, clientKey, token ):

        self.accountUrl= url
        self.authorizedClient= authorizedClient
        self.clientKey= clientKey
        self.token= token
            
        payload = {}
        headers = {
            'AuthorizedClient': self.authorizedClient,
            'ClientKey': self.clientKey,
            'Content-Type': 'application/json',
            'Authorization': self.token
            }
        
        response = requests.request("GET", url, headers=headers, data=payload, verify=False)
        if response.ok:
            response_dic= json.loads(response.text)
            accountNumber= response_dic[0]['accountNumber']
            #cuenta= response_dic[0]['name']
            return accountNumber
        else:
            print("********* Error de conexion " + str(response.status_code) + " *********")

    """Retrieves cash balance available for trading for the given account"""
    def availableCash(self, url, authorizedClient, clientKey, token):
        self.accountUrl= url
        self.authorizedClient= authorizedClient
        self.clientKey= clientKey
        self.token= token

        payload = {}
        headers = {
            'AuthorizedClient': self.authorizedClient,
            'ClientKey': self.clientKey,
            'Content-Type': 'application/json',
            'Authorization': self.token
            }
        
        response = requests.request("GET", url, headers=headers, data=payload, verify=False)
        if response.ok:
            response_dic= json.loads(response.text)
            return response_dic
        else:
            print("********* Error de conexion " + str(response.status_code) + " *********")

    """Retrieves account balance and positions"""

    def balancePosition(self, url, authorizedClient, clientKey, token):
       
        self.accountUrl= url
        self.authorizedClient= authorizedClient
        self.clientKey= clientKey
        self.token= token

        payload = {}
        headers = {
            'AuthorizedClient': self.authorizedClient,
            'ClientKey': self.clientKey,
            'Content-Type': 'application/json',
            'Authorization': self.token
            }
        
        response = requests.request("GET", url, headers=headers, data=payload, verify=False)
        if response.ok:
            response_dic= json.loads(response.text)
            return response_dic
        else:
            print("********* Error de conexion " + str(response.status_code) + " *********")


if __name__== "__main__":

    def json_to_data(jsonFilePath):
        with open(jsonFilePath, "r", encoding = 'utf-8') as json_file:
            data= json.load(json_file)
            bearerToken= data['bearerToken']
            return bearerToken
    
    bearer_token= json_to_data(r'data.json')
    
    #rest_conector= restConector()
    #login= rest_conector.conector(RC.LOGIN_REST_URL, RC.AUTHORIZED_CLIENT, RC.CLIENT_KEY, RC.API_KEY, RC.API_SECRET)
    #bearerToken= login[3]
    accountData= accounts()

    accountNumber= accountData.accountNum(RC.ACCOUNT_URL, RC.AUTHORIZED_CLIENT, RC.CLIENT_KEY, bearer_token)
    print("Número de cuenta: " + accountNumber)
    
    #cash= accountData.availableCash(RC.CASH_URL, RC.AUTHORIZED_CLIENT, RC.CLIENT_KEY,bearerToken)
    #for i in cash:
        #moneda= i["name"]
        #simbolo= i["symbol"]
        #monto= i["amount"]
        #disponibilidad= i["settlement"]
        #print(f"Moneda: {moneda} Monto: {simbolo} {monto} Disponibilidad: {disponibilidad}")

   # balancePosition= accountData.balancePosition(RC.BALANCE_URL, RC.AUTHORIZED_CLIENT, RC.CLIENT_KEY,bearerToken)
    
    #print(balancePosition)
    #groupedAvailability= balancePosition['groupedAvailability']
    #groupedInstruments= balancePosition['groupedInstruments']
    #acciones= groupedInstruments[0]
    #print(acciones)

    """for i in balancePosition:
        for x in balancePosition['groupedInstruments']:
            for y in balancePosition['groupedInstruments'][0]:
                print(y)"""
            
