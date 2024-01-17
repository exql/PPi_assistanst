from conector import restConector
from config import restCredencial as RC
from datetime import  datetime, timedelta
from dateutil import parser

expiresDate= 0

today= datetime.now()
todayStr= today.strftime('%Y-%m-%d %H:%M:%S')
todayDate=datetime.strptime(todayStr, '%Y-%m-%d %H:%M:%S')

if expiresDate == None:
    rest_conector= restConector()
    login= rest_conector.logger(RC.LOGIN_REST_URL, RC.AUTHORIZED_CLIENT, RC.CLIENT_KEY, RC.API_KEY, RC.API_SECRET)
    loginTime= login[0]
    expiresTime= login[1]
    expTime= parser.parse(expiresTime)
    fExpirationStr= expTime.strftime('%Y-%m-%d %H:%M:%S')
    expiresDate=datetime.strptime(fExpirationStr, '%Y-%m-%d %H:%M:%S')
    print('Primera Conexion')

elif todayDate >= expiresDate:

    rest_conector= restConector()
    login= rest_conector.logger(RC.LOGIN_REST_URL, RC.AUTHORIZED_CLIENT, RC.CLIENT_KEY, RC.API_KEY, RC.API_SECRET)
    loginTime= login[0]
    expiresTime= login[1]
    expTime= parser.parse(expiresTime)
    fExpirationStr= expTime.strftime('%Y-%m-%d %H:%M:%S')
    expiresDate=datetime.strptime(fExpirationStr, '%Y-%m-%d %H:%M:%S')
    print('Segunda Conexion')
else:
    print(expiresDate)
    print(type(expiresDate))
    print(todayDate)
    print(type(todayDate))