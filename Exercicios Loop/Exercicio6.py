primos = []
num = 2

while len(primos) < 10:
    primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            primo = False
            break
    if primo:
        primos.append(num)
    num += 1

for p in primos:
    print(p)
