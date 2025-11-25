pares = []
while len(pares) < 30:
    n = int(input("Introduza um numero inteiro entre 1 e 50: "))
    if 1 <= n <= 50 and n % 2 == 0:
        pares.append(n)

media = sum(pares) / 30
print("Media dos 30 numeros pares:", media)
