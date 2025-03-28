sec = int(input("Insira a quantidade de segudos: "))

minutos = sec // 60
horas = minutos // 60
dias = horas // 24

print(f"{sec} segundos dão {dias} dias, {horas} horas e {minutos} minutos")