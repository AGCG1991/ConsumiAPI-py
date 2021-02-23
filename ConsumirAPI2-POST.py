import requests
import json

from requests.models import Response

if __name__ == '__main__' :
    url = 'https://httpbin.org/post'
    payload = { 'nombre' : 'Aitor' , 'curso' : 'python', 'nivel':'intermedio'}
    #Con el método post creamos recursos en el servidor (enviando parámetros)
    """
    Mandaremos los parámetros dentro del "data"
    """
    #response = requests.post(url, json=payload)
    response = requests.post(url, data=json.dumps(payload))
    #json post se encarga de serializarlos
    #data entonces nosotros debemos de serializarlos
    print(response.url)

    if response.status_code == 200:
        print(response.content)