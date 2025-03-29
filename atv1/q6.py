count = 100
n = 2
while count:
    primo = True
    for i in range(2, n):
        if (n % i == 0) and (n != 2):
            primo = False
    
    if primo:
        print(n)
        count -= 1
    n += 1