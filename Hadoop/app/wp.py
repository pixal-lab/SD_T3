import requests
import json

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
    "bugatti"
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
        with open(f'../carpeta1/{entrada}.txt', 'w') as f:
            f.write(texto)
    else:
        with open(f'../carpeta2/{entrada}.txt', 'w') as f:
            f.write(texto)
    with open('../data.txt', 'a') as f:
        f.write(f'{i}\t{url_document}\n')
    i = i + 1

