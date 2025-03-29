ns = []

for i in range (1,4):
    n = int(input(f"Insira o numero {i}: "))
    ns.append(n)

print(f"O maximo e: {max(ns)}")
print(f"O minimo e: {min(ns)}")