import json

def save_estoque(estoque):
    if len(estoque):
        with open('estoque.json', 'w') as file:
            json.dump(estoque, file, indent=4)
        print("Estoque salvo com sucesso.")