pares = 0
impares = 0
num = 1

while pares < 30 or impares < 30:
    if num % 2 == 0:
        if pares < 30:
            print(num)
            pares += 1
    else:
        if impares < 30:
            print(num)
            impares += 1
    num += 1