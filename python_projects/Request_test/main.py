import requests 

headers = {'Content-Type' : 'application/json',
          'trainer_token' : 'USER_TOKEN'}
host = 'https://api.pokemonbattle.ru/v2'
body_create = {
    "name": "python",
    "photo_id": -1
}
body_name = {
    "pokemon_id": "POKEMON_ID",
    "name": "generate",
    "photo_id": -1
}
body_pokeball = {
    "pokemon_id": "POKEMON_ID"
}

response1 = requests.post (url= f'{host}/pokemons', headers= headers, json= body_create)
print(response1.text)

response2 = requests.put (url= f'{host}/pokemons' , headers= headers, json= body_name)
print(response2.text)

response3 = requests.post (url= f'{host}/trainers/add_pokeball', headers= headers, json= body_pokeball)
print(response3.text)
