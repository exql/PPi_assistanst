import requests
import json
import urllib3
from config import restCredencial as RC
from conector import restConector
from token_manager import tokenManager

    
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


""" Retrieves all data of the available accounts 
Account Number
Cash balance available for trading
Positions
Account Movements
"""

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

    importador= tokenManager()   
    credenciales= importador.importer(r'data.json')

    bearerToken= credenciales[3]
    accountData= accounts()

    accountNumber= accountData.accountNum(RC.ACCOUNT_URL, RC.AUTHORIZED_CLIENT, RC.CLIENT_KEY, bearerToken)
    print('Número de cuenta: ' + accountNumber)
    
    print("Dinero Disponible: ")
    cash= accountData.availableCash(RC.CASH_URL, RC.AUTHORIZED_CLIENT, RC.CLIENT_KEY, bearerToken)
    for i in cash:
        moneda= i["name"]
        simbolo= i["symbol"]
        monto= i["amount"]
        disponibilidad= i["settlement"]
        print(f"Moneda: {moneda} Monto: {simbolo} {monto} Disponibilidad: {disponibilidad}")

    print("Estado de cuenta ")
    balancePosition= accountData.balancePosition(RC.BALANCE_URL, RC.AUTHORIZED_CLIENT, RC.CLIENT_KEY,bearerToken)
    
    #print(balancePosition)
    groupedAvailability= balancePosition['groupedAvailability']
    groupedInstruments= balancePosition['groupedInstruments']
    acciones= groupedInstruments[0]
    accion=groupedInstruments[0]['instruments']
    
    
    for i in accion:
        simbolo= i["ticker"]
        nombre= i["description"]
        ultimoPrecio= i["price"]
        valorCorriente= i["amount"]
        cantidad=int(int(valorCorriente)/int(ultimoPrecio))
        #print(f"Especie: {simbolo} Nombre: {nombre} Cantidad {cantidad} Precio:$ {ultimoPrecio} valorCorriente:$ {valorCorriente}")
        print( "Especie    Cantidad  Precio  valorCorriente:")
        print(f"{simbolo} {cantidad} ${ultimoPrecio}  ${valorCorriente}")

    #cedear= groupedInstruments[1]['instruments']
    
    #print(accion)
    #print(cedear)
    
"""
    for i in balancePosition:
        for x in balancePosition['groupedInstruments']:
            for y in balancePosition['groupedInstruments'][0]:
                print(y)
            
"""