import requests
import pytest


host = 'https://api.pokemonbattle.ru/v2'
trainer_id = 36810 


def test_status200():
    response1 = requests.get (url= f'{host}/trainers', params= {'trainer_id': trainer_id})
    assert response1.status_code ==200

def test_part_of_response():
    response2 = requests.get (url= f'{host}/trainers', params= {'trainer_id': trainer_id})
    assert response2.json()['data'][0]['trainer_name'] == 'Meow'
