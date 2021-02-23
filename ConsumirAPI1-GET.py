import requests
import json

if __name__ == '__main__' :
    url = 'https://httpbin.org/get'
    args ={ 'nombre' : 'Aitor' , 'curso' : 'python', 'nivel':'intermedio'}
    #Tras el ? inicio una query que le da valores
    response = requests.get(url, params=args)
    #El método get construyle la url con los argumentos que nosotros le pasamos
    print(response.url)

        #Si me responde con un código 200
    if response.status_code == 200:
        """
        response_json=response.json() #Diccioario
        origin = response_json['origin']
        print(origin)
        """
        response_json = json.loads(response.text)
        origin = response_json['origin']
        print(origin)