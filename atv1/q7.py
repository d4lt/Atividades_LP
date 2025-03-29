while True:
    odd = int(input("Insira um numero impar: "))
    if odd%2 != 0:
        break

quadrado = (odd-1)**2
prox_odd = odd+2
diff = quadrado - prox_odd

print(f"A diferença entre o quadrado do número anterior e do próximo número ímpar e: {diff}")