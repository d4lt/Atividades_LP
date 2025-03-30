print("Seja bem-vindo ao sistema de login!")

while True:
    usuario = input("Insira o nome de usuário: ")
    senha = input("Insira a senha: ")

    if usuario == senha:
        print("Por favor, repita. O nome de usuário e senha não podem ser iguais.")
    else:
        break

print("Login feito com sucesso!")