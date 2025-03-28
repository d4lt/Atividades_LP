valor_total = float(input("Insira o valor total das compras: "))

if valor_total < 500:
    print("Não há imposto sobre valores menores que 500 reais.")
else:
    print(f"O valor final após a taxação é: {valor_total*1.5}")