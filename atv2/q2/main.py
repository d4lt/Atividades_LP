import json
from save_estoque import save_estoque


# def safe_guard(var, message, lower_limit, upper_limit=0, ):
#     pass

def fetch_estoque() -> list:
    try:
        with open('estoque.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def adicionar_produto(nome, quantidade, preco):
    produto = { 
               'nome': nome,
               'quantidade': quantidade,
               'preco': preco
                }
    
    estoque.append(produto)
    print(f'\nProduto "{nome}" adicionado com sucesso.')

def main():
    print("Bem-vindo ao gerenciador de estoque\n")
    
    while True:
        
        print("[1] Adicionar produto")
        print("[2] Exibir produtos")
        print("[3] Sair\n")
        
        comando = input("O que você deseja fazer?\n>> ").strip()
        
        if comando == '1':
            nome_produto = input("\nDigite o nome do produto: ")
            while True:
                quantidade_produto = int(input("Digite a quantidade do produto: "))
                if quantidade_produto > 0:
                    break
                else:
                    print("A quantidade deve ser maior que zero.")

            while True:                
                preco_produto = float(input("Digite o preço do produto: "))
                if preco_produto > 0:
                    break
                else:
                    print("O preço deve ser maior que zero.")
            adicionar_produto(nome_produto, quantidade_produto, preco_produto)
        elif comando == '2':
            if not estoque:
                print("Nenhum produto cadastrado.")
            else:
                print("\nProdutos cadastrados:\n")
                print("Qtnd   Nome   Valor")

                for produto in estoque:
                    print(f"{produto['quantidade']}  {produto['nome']}   {produto['preco']:.2f}")
                    
                precos = [produto['preco']*produto['quantidade'] for produto in estoque]
                print(f"\nVALOR TOTAL DO ESTOQUE: {sum(precos)}\n\n")
                
        elif comando == '3':
            save_estoque(estoque)
            print("Saindo do programa...")
            break

estoque = fetch_estoque()

if __name__ == "__main__":
    main()