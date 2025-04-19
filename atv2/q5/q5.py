import save_contatos

contatos = save_contatos.fetch_contatos()
def main():
    print("Bem-vindo ao gerenciador de contatos!")
    
    while True:
        print("[1] Adicionar contato")
        print("[2] Buscar contatos")
        print("[3] Sair")

        comando = input("O que você deseja fazer?\n>>").strip()
        
        if comando == '1':
            name_contato = input("Qual o nome do contato?: ").strip()
            phone_contato = input("Qual o telefone do contato?: ").strip()
            email_contato = input("Qual o email do contato?: ").strip()
            
            new_contato = {
                'nome': name_contato,
                'phone': phone_contato,
                'email': email_contato
            }
            contatos.append(new_contato)
            print("Novo contato salvo com sucesso!\n")
        
        if comando == '2':
            name = input("Nome do contato a procurar: ")
            contatos_found = []

            contato_exists = False
            for contato in contatos:
                if contato['nome'] == name:
                    contatos_found.append(contato)
            
            if contatos_found:
                if len(contatos_found) == 1:
                    print("Contato encontrado!")
                    print(*contatos_found[0])
                else:
                    print("Aqui estão alguns contatos com esse nome:\n")
                    for contato in contatos_found:
                        print(f"{contato['nome']} {contato['phone']} {contato['email']}")
                
            else:
                print("Não foi possível encontrar um contato com esse nome\n")
        
        elif comando == '3':
            save_contatos.save_contatos(contatos)
            break

if __name__ == "__main__":
    main()