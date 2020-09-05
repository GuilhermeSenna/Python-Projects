import requests
try:
    response = requests.get('http://www.pudim.com.br')
except:
    print('O site Pudim não está disponivel no momento.')
else:
    print('O Site pudim está disponivel no momento.')
#print(response.status_code)