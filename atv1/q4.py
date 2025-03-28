km = int(input("Quantidade de Km rodados: "))
dias = int(input("Dias rodados: "))

if km < 100:
    print(f"O valor total a ser pago é: {dias*90} reais.")
else:
    print(f"O valor total a ser pago é: {dias*90 + km*12} reais.")