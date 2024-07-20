import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '31ec73a195fd77b5d63c06983e70463a'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}

body_create = {
    "name": "Ванесса",
    "photo_id": 12
}
body_name_change = {
    "pokemon_id": "44414",
    "name": "Vanessa",
    "photo_id": 12
}
body_pokeball = {
    "pokemon_id": "44414"
}


response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

response_name_change = requests.put(url = f'{URL}/pokemons',headers = HEADER, json = body_name_change)
print(response_name_change.text)

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball',headers = HEADER, json = body_name_change)
print(response_pokeball.text)
