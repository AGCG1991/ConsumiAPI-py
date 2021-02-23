import requests

if __name__ == '__main__' :
    url = 'https://www.google.com.mx'
    response = requests.get(url)

    print(response)
        #Si me responde con un código 200
    if response.status_code == 200:
        #Guardo el contenido en la variable content (voy a obtener un código html)
        content = response.content 
        #Creo un fichero tipo binario donde guardaré el contenido.
        file =open('Google.html', 'wb')
        file.write(content)
        file.close()