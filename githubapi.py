
#Autentificar en sitios web/aplicaciones móviles
"""
Te puedes autentificar rellenando un formulario de forma manual o utilizando una red social
"""

import requests
#El id no debería estar ahí si no en variables de entorno o en algún sitio seguro
client_id = '3cc3867780b35bc8fdff'
client_secret = '0044b601734f7b8199d40f2c76e9cfffd34d0174'
##https://github.com/login/oauth/authorize?client_id=3cc3867780b35bc8fdff&scope

#Creo una variable CODE, con el hash que se genera al validarme con mi cuenta de github
code ='9025bf303e921eb5b4cb'

if __name__ == '__main__' :

    url='https://github.com/login/oauth/access_token'
    #Le tengo que pasar como parámetro client_id, client_secret y code
    payload = {'client_id': client_id, 'client_secret': client_secret, 'code': code}
    headers = {'Accept': 'application/json'}

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        response_json=response.json()
        #De lo que recibo, le digo que coja acces_token
        access_token = response_json['access_token']
        print(access_token)
        #OJO, la sesión caduca y hay que cambiar el code