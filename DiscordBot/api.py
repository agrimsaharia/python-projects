import requests 
import json

dad_joke_url = "https://dad-jokes.p.rapidapi.com/random/joke"

dad_joke_headers = {
    'x-rapidapi-key': "a8703ff064msh7a09c106cbbb443p1425f2jsn3dddefa8add1",
    'x-rapidapi-host': "dad-jokes.p.rapidapi.com"
    }

def get_dad_joke():
    response = requests.request("GET", dad_joke_url, headers=dad_joke_headers)
    joke_body = json.loads(response.text)['body'][0]
    return joke_body