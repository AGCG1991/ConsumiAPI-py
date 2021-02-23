import requests
import json

if __name__ == '__main__' :
    url = 'https://httpbin.org/post'
    payload = { 'nombre' : 'Aitor' , 'curso' : 'python', 'nivel':'intermedio'}

    #Le digo al servidor que estoy enviando datos a un json
    headers = {'Content-Type' : 'application/json', 'access-token': '12345'}
 
    response = requests.post(url, data=json.dumps(payload), headers=headers)
  
    print(response.url)

    if response.status_code == 200:
        #print(response.content)
        headers_response =response.headers #Diccionario
        #print(headers_response)
        server= headers_response['Server']
        print(server)