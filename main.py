import os 
import requests 
import json 

pokemon_choice = input("Enter a pokemon's name\n") 

response = requests.get(f"http://pokeapi.co/api/v2/pokemon/{pokemon_choice}/")
# response = requests.get(f"http://pokeapi.co/api/v2/pokemon/pikachu/")
body = json.loads(response.content) 



# print(poke_type)


try: 

    body = json.loads(response.content) 
    poke_name = body['name']
    poke_id = body['id']
    poke_type = body['types'][0]['type']['name']

    string = f"You caught {poke_name}, id: {poke_id}, type: {poke_type}"

    print(string)

except: 
    print('No pokemon found') 




# body = json.loads(response.content) 
# print("You caught {}".format(body["name"]))
