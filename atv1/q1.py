notas = [] 

for i in range(1,4):
    nota = int(input(f"insira a nota {i}:"))
    notas.append(nota)

print(f"Media: {sum(notas)/3}")
print(f"Media Ponderada (2,2,3): {(2*notas[0] + 2*notas[1] + 3*notas[2])/7}")
print(f"Media Ponderada (1,2,2): {(1*notas[0] + 2*notas[1] + 2*notas[2])/5}")