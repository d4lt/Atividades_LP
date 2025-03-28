count = 100
n = 2
while count:
    for i in range(2, n):
        if (n == 2) or (n % i != 0):
            print(n)

            count -= 1
            n += 1