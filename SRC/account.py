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
    def accountNum(self, accountUrl, authorizedClient, clientKey, bearerTokentoken ):

        self.accountUrl= accountUrl
        self.authorizedClient= authorizedClient
        self.clientKey= clientKey
        self.bearerTokentoken= bearerTokentoken

        url= self.accountUrl + "Account/Accounts"

        payload = {}
        headers = {
            'AuthorizedClient': self.authorizedClient,
            'ClientKey': self.clientKey,
            'Content-Type': 'application/json',
            'Authorization': self.bearerTokentoken
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
    def availableCash(self, url, authorizedClient, clientKey, bearerTokentoken):
        self.accountUrl= url
        self.authorizedClient= authorizedClient
        self.clientKey= clientKey
        self.bearerTokentoken= bearerTokentoken

        payload = {}
        headers = {
            'AuthorizedClient': self.authorizedClient,
            'ClientKey': self.clientKey,
            'Content-Type': 'application/json',
            'Authorization': self.bearerTokentoken
            }
        
        response = requests.request("GET", url, headers=headers, data=payload, verify=False)
        if response.ok:
            response_dic= json.loads(response.text)
            return response_dic
        else:
            print("********* Error de conexion " + str(response.status_code) + " *********")

    """Retrieves account balance and positions"""

    def balancePosition(self, url, authorizedClient, clientKey, bearerTokentoken):
       
        self.accountUrl= url
        self.authorizedClient= authorizedClient
        self.clientKey= clientKey
        self.bearerTokentoken= bearerTokentoken

        payload = {}
        headers = {
            'AuthorizedClient': self.authorizedClient,
            'ClientKey': self.clientKey,
            'Content-Type': 'application/json',
            'Authorization': self.bearerTokentoken
            }
        
        response = requests.request("GET", url, headers=headers, data=payload, verify=False)
        if response.ok:
            response_dic= json.loads(response.text)
            return response_dic
        else:
            print("********* Error de conexion " + str(response.status_code) + " *********")
    

    """Retrieves movements for the given account between the specified dates."""
    def accountMovement(self, baseUrl, authorizedClient, clientKey, bearerTokentoken, dateFrom, dateTo, ticker):

        self.baseUrl=baseUrl
        self.authorizedClient= authorizedClient
        self.clientKey= clientKey
        self.bearerTokentoken= bearerTokentoken
        self.dateFrom= dateFrom
        self.dateTo= dateTo
        self.ticker=ticker
        
        accountData= accounts()
        accountNumber= accountData.accountNum(self.baseUrl, self.authorizedClient, self.clientKey, self.bearerTokentoken)
        
        url= self.baseUrl + f"Account/Movements?accountNumber={accountNumber}&dateFrom={self.dateFrom}&dateTo={self.dateTo}&ticker={self.ticker}"
        payload = {}
        headers = {
        'AuthorizedClient': self.authorizedClient,
        'ClientKey': self.clientKey,
        'Content-Type': 'application/json',
        'Authorization': self.bearerTokentoken
        }

        response = requests.request("GET", url, headers=headers, data=payload, verify=False)

        if response.ok:
            response_dic= json.loads(response.text)
            return response_dic

if __name__== "__main__":

    importador= tokenManager()   
    credenciales= importador.importer(r'data.json')
    bearerToken= credenciales[3]
    accountData= accounts()

    accountNumber= accountData.accountNum(RC.BASE_URL, RC.AUTHORIZED_CLIENT, RC.CLIENT_KEY, bearerToken)
    #print('Número de cuenta: ' + accountNumber)
    
    #---------------- Probando available Cash
    #print("Dinero Disponible: ")
    #cash= accountData.availableCash(RC.CASH_URL, RC.AUTHORIZED_CLIENT, RC.CLIENT_KEY, bearerToken)
    #for i in cash:
        #moneda= i["name"]
        #simbolo= i["symbol"]
        #monto= i["amount"]
        #disponibilidad= i["settlement"]
        #print(f"Moneda: {moneda} Monto: {simbolo} {monto} Disponibilidad: {disponibilidad}")

    
    #-------------- Probando Balance Position
    #print("Estado de cuenta ")
    #balancePosition= accountData.balancePosition(RC.BALANCE_URL, RC.AUTHORIZED_CLIENT, RC.CLIENT_KEY,bearerToken)
    
    #print(balancePosition)
    #groupedAvailability= balancePosition['groupedAvailability']
    #groupedInstruments= balancePosition['groupedInstruments']
    #acciones= groupedInstruments[0]
    #accion=groupedInstruments[0]['instruments']
    
    
   #for i in accion:
    #    simbolo= i["ticker"]
    #    nombre= i["description"]
    #    ultimoPrecio= i["price"]
    #   valorCorriente= i["amount"]
    #    cantidad=int(int(valorCorriente)/int(ultimoPrecio))
    #    #print(f"Especie: {simbolo} Nombre: {nombre} Cantidad {cantidad} Precio:$ {ultimoPrecio} valorCorriente:$ {valorCorriente}")
    #    print( "Especie    Cantidad  Precio  valorCorriente:")
    #    print(f"{simbolo} {cantidad} ${ultimoPrecio}  ${valorCorriente}")

    #cedear= groupedInstruments[1]['instruments']
    
        
    # -------------- Probando accountMovement
    """
    dateFrom= "2020-01-01"
    dateTo= "2023-06-30"
    ticker= "GGAL"

    baseUrl= 'https://clientapi_sandbox.portfoliopersonal.com/api/1.0/'
    
    movimiento=accountData.accountMovement(RC.BASE_URL, RC.AUTHORIZED_CLIENT, RC.CLIENT_KEY, bearerToken, dateFrom, dateTo, ticker)
    #for i in movimiento:
    #   print(i)
    for i in movimiento:
      
        fechaAcuerdro= i['agreementDate']
        fechaLiquidacion= i['settlementDate']
        moneda= i['currency']
        importe= i['amount']
        precioActivo= i['price']
        tipoOperacion= i['description']
        ticker= i['ticker']
        cantidad= i['quantity']
        balance= i['balance']  

        print(f'Movimiento {tipoOperacion}')
        texto= f"fecha: {fechaLiquidacion} Descripción: {tipoOperacion} Cantidad: {cantidad} Precio:{precioActivo} Importe:{importe} Saldo:{balance}"
        print(texto)
        print('-'*10)
    """