import requests
import json
import sys

#Declaramos una función
"""
No podemos listar todos los pokemon de una vez (No lo permite la API), pero tiene un offset que delimita cuantos 
se pueden listar de una vez, con un método recursivo que llame a la función y vaya incrementando el valor del offset
podremos ir listando todos
"""
def get_pokemons(url='http://pokeapi.co/api/v2/pokemon-form', offset=0):
    args = {'offset': offset} if offset else {}
        


    response = requests.get(url, params=args)
    if response.status_code ==200:

        payload = response.json()
        results =payload.get('results', [])

        if results:
            for pokemon in results:
                name = pokemon ['name']
                print(name)

                #input() permite absorber contenido de teclado
                next=input("¿Continuar listando? [Y/N]").lower()
                if next == 'y' :
                    get_pokemons(offset=offset+20)

if __name__ == '__main__' :
    url = 'http://pokeapi.co/api/v2/pokemon-form'
    get_pokemons()
