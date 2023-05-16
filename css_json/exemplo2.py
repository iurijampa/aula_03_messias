import json

list = {
    'frutas': ['acabate', 'uva', 'uva', 'kiwi'],
    'data': '2023-05-20'
}
with open('arquivo.json', 'w') as arquivo:
    json.dump(list, arquivo)
    meu_json = json.dumps(list)
    