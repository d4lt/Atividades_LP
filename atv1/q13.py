salario_inicial = int(input("Insira o salário inicial: "))
aumento = float(input("Insira o aumento percentual (ao ano): "))
anos = int(input("Insira a quantidade de anos decorridos: "))

# n entendi mt bem como funciona o aumento :(
salario_final = salario_inicial * (1 + aumento)**anos

print(f"O salário final será: {salario_final}")