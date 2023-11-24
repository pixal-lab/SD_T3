import requests
import json
import os

if not os.path.exists("carpeta1"):
    os.makedirs("carpeta1")

if not os.path.exists("carpeta2"):
    os.makedirs("carpeta2")

entradas = [
    "mazda", 
    "nissan", 
    "toyota",
    "mitsubishi",
    "suzuki", 
    "bentley", 
    "ferrari", 
    "lamborghini",
    "lotus", 
    "bugatti",

    "Jaws_(film)",
    "Star_Wars_(film)",
    "The_Matrix",
    "Pulp_Fiction",
    "The_Godfather",

    "Titanic_(1997_film)",
    "The_Shawshank_Redemption",
    "Jurassic_Park",
    "The_Dark_Knight",
    "Inception",

    "The_Legend_of_Zelda",
    "Super_Mario_Bros",
    "Minecraft",
    "Grand_Theft_Auto_V",
    "The_Elder_Scrolls_V",

    "World_of_Warcraft",
    "Fortnite",
    "Pokemon",
    "League_of_Legends",
    "Dota_2",

]
url = "https://en.wikipedia.org/w/api.php"
i = 1
for entrada in entradas:
    params = {
        'format': 'json',
        'action': 'query',
        'prop': 'extracts|info',
        'inprop': 'url',
        'exintro': '',
        'explaintext': '',
        'redirects': 1,
        'titles': entrada
    }

    req = requests.get(
        url,
        params=params
    ).json()

    n_page = list(req['query']['pages'].keys())[0]
    texto = req['query']['pages'][n_page]['extract']
    texto = '{}<splittername>{}'.format(i, json.dumps(texto))
    url_document = req['query']['pages'][n_page]['fullurl']

    if i <= 15:
        try:
            with open(f'carpeta1/{entrada}.txt', 'w') as f:
                f.write(texto)
        except:
            with open(f'carpeta1/{entrada}.txt', 'a') as f:
                f.write(texto)
    else:
        try:
            with open(f'carpeta2/{entrada}.txt', 'w') as f:
                f.write(texto)
        except:
            with open(f'carpeta2/{entrada}.txt', 'a') as f:
                f.write(texto)
    with open('data.txt', 'a') as f:
        f.write(f'{i}\t{url_document}\n')
    i = i + 1

