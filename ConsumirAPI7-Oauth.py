
#Autentificar en sitios web/aplicaciones móviles
"""
Te puedes autentificar rellenando un formulario de forma manual o utilizando una red social
"""

import requests
#El id no debería estar ahí si no en variables de entorno o en algún sitio seguro
client_id = 'd267134110a0483ccd1b'
client_secret = 'c79e0948a4b2152999d6acc3686a295b0e992461'
##https://github.com/login/oauth/authorize?client_id=d267134110a0483ccd1bfdff&scope
"""
El token tiene una duración de 2 h normalmente
"""

#Creo una variable CODE, con el hash que se genera al validarme con mi cuenta de github
code ='c9b990916ebdf833fa34'

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

        #El access_token que nos devuelve es 3b972583959557add79748369d8ff0d8533e3b1e