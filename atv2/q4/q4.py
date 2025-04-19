usuarios = []
transacoes = []

def main():
    usuario_logged = False
    print("Bem-vindo ao sistema bancário SenaBan\n")

    while True:
        print("[1] Entrar")
        print("[2] Cadastrar usuário")
        print("[3] Fazer transação\n")

        comando = input("O que você deseja fazer? (para sair digite 'sair')\n>>").strip().lower()
        
        if comando == '1':
            nome_usuario = input("Nome de usuário: ").strip().lower()
            senha_usuario = input("Senha de usuário: ").strip()
            usuario_existente = None
            for usuario in usuarios:
                if usuario['nome'] == nome_usuario:
                    usuario_existente = usuario
            if usuario_existente is not None and senha_usuario == usuario_existente['senha']:
                  usuario_logged = True
                  print("Login realizado com sucesso!\n")
            else:
                print("Nome de usuário ou(e) senha incorreto.")      
        elif comando == '2':
            while True:
                nome_usuario = input("Informe o nome de usuário: ").strip()
                senha_usuario = input("Informe a senha de usuário: ").strip()
                if nome_usuario in [usuario['nome'] for usuario in usuarios]:
                    print("Este nome já existe, por favor crie um novo.")
                else:
                    break
            new_usuario = { 
                           'nome': nome_usuario,
                           'senha': senha_usuario     
                           }
            usuarios.append(new_usuario)
            print("Usuário adicionado com sucesso!")
        
        elif comando == '3':
            if not usuario_logged:
                print("Você precisa estar logado para fazer uma transação.")
                continue
            
            nome_usuario = input("Informe o nome de usuário: ").strip()
            
            while True:
                valor_transacao = float(input("Informe o valor da transação: "))
                if valor_transacao > 0:
                    break
                else:
                    print("O valor deve ser maior que zero.")
            
            while True:
                tipo_transacao = input("Informe o tipo de transação (saque/deposito): ").strip().lower()
                if tipo_transacao not in ['saque', 'deposito']:
                    print("Tipo de transação inválido.")
                else:
                    break

            transacao = {
                'usuario': usuario_logged,
                'valor': valor_transacao,
                'tipo': tipo_transacao
            }
            
            print("Transação realizada com sucesso!")
            transacoes.append(transacao)
            print("Transações:", transacoes)
            
            

if __name__ == "__main__":
    main()