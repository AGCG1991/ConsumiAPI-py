import requests
import json
#Con Delete eliminamos un recurso del servidor
#Con Put actualizamos un recurso
if __name__ == '__main__' :
    url = 'https://httpbin.org/put'
    payload = { 'nombre' : 'Aitor' , 'curso' : 'python', 'nivel':'intermedio'}

    #Le digo al servidor que estoy enviando datos a un json
    headers = {'Content-Type' : 'application/json', 'access-token': '12345'}
    response = requests.put(url, data=json.dumps(payload), headers=headers)
    """
    GET-> Obtener recursos
    POST -> Crear recursos
    PUT -> Actualizarlo (modificar valores)
    DELETE -> Eliminarlo
    """
    print(response.url)

    if response.status_code == 200:
        headers_response =response.headers #Diccionario
        server= headers_response['Server']
        print(server)