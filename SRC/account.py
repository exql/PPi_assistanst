import requests
import json
import urllib3
from config import restCredencial as RC
from conector import restConector
    
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


""" Retrieves all the available accounts """
class accounts:

    """"""
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

            """print(response_dic)
            print('Account Number: ')
            print(accountNumber)
            print('Cuenta: ')
            print(cuenta)"""
        else:
             print(response)
        return accountNumber






if __name__== "__main__":

    acc



    token= "bearer " + ""
    accountData= accounts()
    accountNumber= accountData.accountNum(RC.ACCOUNT_URL, RC.AUTHORIZED_CLIENT, RC.CLIENT_KEY,token)
    print(accountNumber)
    