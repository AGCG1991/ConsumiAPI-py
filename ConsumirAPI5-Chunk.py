import requests
import json

if __name__ == '__main__':
    url = 'http://i.imgur.com/n9z3sLg.jpg'

    response = requests.get(url, stream=True) #Realiza la petición sin descagar contenido
    #Con Stream=True dejamos la conexión abierta para que se pueda descargar el fichero
    with open('image.jpg', "wb") as file:
        for chunk  in response.iter_content(): #Descarga el contenido poco a poco
            file.write(chunk)
    response.close() # Forzamos el cierre de la conexión nosotros
    """
    Normalmente al hacer una petición, el tiempo de respuesta es limitado, es decir al ser respondida la consulta
    se cierra la conexión
    """