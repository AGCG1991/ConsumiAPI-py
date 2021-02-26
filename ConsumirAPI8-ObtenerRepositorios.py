
#Autentificar en sitios web/aplicaciones móviles
"""
Te puedes autentificar rellenando un formulario de forma manual o utilizando una red social
"""

import requests
#El id no debería estar ahí si no en variables de entorno o en algún sitio seguro
client_id = 'd267134110a0483ccd1b'
client_secret = 'c79e0948a4b2152999d6acc3686a295b0e992461'
##https://github.com/login/oauth/authorize?client_id=d267134110a0483ccd1b&scope
"""
El token tiene una duración de 2 h normalmente
"""

#Creo una variable CODE, con el hash que se genera al validarme con mi cuenta de github
code ='b0476adbb48dee2933cb'
access_token = '3b972583959557add79748369d8ff0d8533e3b1e'

if __name__ == '__main__' :
        url = 'https://api.github.com/user/repos'
        headers = {"Authorization" : 'token 3b972583959557add79748369d8ff0d8533e3b1e'}

        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            payload =response.json()
            for project in payload:
                name=project['name']
                print(name)
        else :
            print(response.content)
