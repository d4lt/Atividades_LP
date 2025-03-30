n = int(input("Insira um numero inteiro maior que 1: "))

is_prime = True
for i in range(2,n):
    if n != 2 and n%i == 0:
        is_prime = False

if is_prime:
    print("O numero e primo!")
else:
    print("O numero nao e primo!")