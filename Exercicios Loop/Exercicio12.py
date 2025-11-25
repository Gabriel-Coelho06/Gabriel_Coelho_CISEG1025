n = int(input("Introduza um numero: "))
operacoes = 0

for i in range(1, n):
    print(n, "+", i, "=", n+i)
    operacoes += 1
    print(n, "-", i, "=", n-i)
    operacoes += 1
    print(n, "*", i, "=", n*i)
    operacoes += 1
    print(n, "/", i, "=", n/i)
    operacoes += 1

print("Total de operacoes efetuadas:", operacoes)
