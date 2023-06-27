import csv
import requests
import jwt
import json
import pandas as pd
from keycloak import KeycloakOpenID
import requests
#from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Deshabilitar los warnings relacionados con la verificación de certificados SSL
#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

armz = 'https://dev-servicos-oliveiratrust.scot.oliveiratrust.com/api-armazenamento/api/v1/file/'
accessTokenUrl = "https://keycloak.qa.fintools.dev.br/auth/realms/Restrito/protocol/openid-connect/token"
client_secret = 'bN5UsLVuKX4eG250m0GFsFhHdCV0F1NQ' # client secret do cliente do Keycloak
client_id = 'api-contratos' # client id do cliente do Keycloak
grant_type = 'client_credentials' # tipo de autenticação
payload = 'client_id='+client_id+'&grant_type='+grant_type+'&client_secret='+client_secret

headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", accessTokenUrl, headers=headers, data=payload)
p = 'j7iYpnhTHv1TZg8fUolCXb0XvrqbbB-XrSh9SGR4SAIM5QnjlNt4eUrwfYj9iTyMRk9Q73H7mDMCa7go2x9VUO_Shx6mJGStWOM4Lpmyeo1I6UPA7L920X6G0IQQ3VdSXVmqJ5pYTXruJdnIyA_1czx6CbIv0qxKWuvUhAdmlrFYmQiiBcBaDO319aLFFavTwAtThKBojVNogbLftMjb6hGHlznYfaEGWTQC5nffe1Ta5d4Tl61kXiBMehPAHffR-RZfZ6NUUCtZXAdk3DL5-dBe6AxMn9vbJ5NfxgL-BUY1uv3Yhp0ncpMS-z0JKtEYz3SBq1gpevehnd9C_Q7jgQ"'
access_token = response.json()['access_token']

print(access_token)

headers = {
  'Authorization': 'Bearer '+access_token,
  'Realm': 'Restrito',
  
}

resp = requests.request('POST', armz, headers=headers)



# with open('teste_armazenamento.txt', 'rb') as f:
#     response = requests.post(
#         'https://dev-servicos-oliveiratrust.scot.oliveiratrust.com/api-armazenamento/api/v1/file/',
#         files={'file': f},
#         headers={'Authorization': f'Bearer {access_token}', 'Realm': 'Restrito'}
#     )




















# decoded_token = jwt.decode(access_token, key=PUBLIC_KEY, algorithms=['RS256'])
# pedidos = {"pedidos": [{ "vendedor": 1, "data": "2022-03-01","valor":500.34 }, 
#     { "vendedor": 1, "data": "2022-03-01", "valor":1000.22 }, 
#     { "vendedor": 1, "data": "2022-03-01", "valor":100.35 }, 
#     { "vendedor": 1, "data": "2022-03-01", "valor":22.34 }, 
#     { "vendedor": 1, "data": "2022-04-01", "valor":5000.34 }, 
#     { "vendedor": 2, "data": "2022-03-01", "valor":2000.34 }, 
#     { "vendedor": 2, "data": "2022-04-01", "valor":3000.34 }, 
# ]}

# pedidos = pd.DataFrame(pedidos['pedidos'])
# print(pedidos)