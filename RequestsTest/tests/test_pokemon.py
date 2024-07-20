import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '31ec73a195fd77b5d63c06983e70463a'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = 4578
def test_status_code_trainers():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200
def test_trainer_name():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'VanGogh'
    