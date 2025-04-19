import json

def save_contatos(contatos):
    if len(contatos):
        with open('contatos.json', 'w') as file:
            json.dump(contatos, file, indent=4)
        print("Estoque salvo com sucesso!")

def fetch_contatos():
    try:
        with open('contatos.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
        