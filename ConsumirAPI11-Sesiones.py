import requests
from requests.models import ContentDecodingError

if __name__ == '__main__' :
    url='https://api.github.com/user'

    session = requests.session()
    session.auth= ('correo@correo.com','contraseña') #Tupla, primer valor es el usuario y el segundo es la contraseña

    response =session.get(url)

    if response.ok  :
         response= session.get('https://github.com/AGCG1991')
         if response.ok  :
            print(response.cookies)