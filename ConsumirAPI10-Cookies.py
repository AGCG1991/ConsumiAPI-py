import requests

if __name__ == '__main__' :
      url = 'https://httpbin.org/get'
      Cookies = {'my-cookie' : 'true'}
      response = requests.get(url,cookies=Cookies)

      if response.ok: #Devuelve verdadero o falso dependiendo si se hizo correctamente o no
          cookies = response.cookies
          print(cookies)

          print("El contenido es :")
          print(response.content)
