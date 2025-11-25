limite = int(input("Introduza um limite: "))
cont_perfeitos = 0

for n in range(1, limite+1):
    soma_divisores = sum(i for i in range(1, n) if n % i == 0)
    if soma_divisores == n:
        cont_perfeitos += 1

print("Quantidade de numeros perfeitos:", cont_perfeitos)
