# O MENU APARECE APOIS A PRIMEIRA :FASE: DO EXERCICIO, PODE OBTAR POR CANCELAR OU SIMPLESMENTE DIZER QUE SIM ATE AO FIM DO NUMERO ESCOLHIDO.
def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def divisores(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count

def perfeito(n):
    return sum(i for i in range(1, n) if n % i == 0) == n


while True:
    valor = int(input("Introduza um valor entre 1 e 30000: "))
    if 1 <= valor <= 30000:
        break

contador = 0
for n in range(valor, 0, -1):
    print("Numero:", n)
    print("Primo:", primo(n))
    print("Divisores:", divisores(n))
    print("Perfeito:", perfeito(n))
    contador += 1
    if contador % 10 == 0 and n != 1:
        opcao = input("Continuar? (s/n): ")
        if opcao.lower() != "s":
            break

while True:
    print("\nMenu:")
    print("1 - Soma")
    print("2 - Subtracao")
    print("3 - Multiplicacao")
    print("4 - Divisao")
    print("5 - Tabuada")
    print("6 - Sair")
    
    escolha = input("Escolha uma opcao: ")

    if escolha == "6":
        break
    elif escolha in ["1","2","3","4"]:
        a = float(input("Valor A: "))
        b = float(input("Valor B: "))
        if escolha == "1":
            print("Resultado:", a+b)
        elif escolha == "2":
            print("Resultado:", a-b)
        elif escolha == "3":
            print("Resultado:", a*b)
        elif escolha == "4":
            if b != 0:
                print("Resultado:", a/b)
            else:
                print("Erro: divisao por zero")
    elif escolha == "5":
        while True:
            max_tab = int(input("Tabuada de 1 ate (1-1000): "))
            if 1 <= max_tab <= 1000:
                break
        for n in range(1, max_tab+1):
            for i in range(1, max_tab+1):
                print(n, "x", i, "=", n*i)
                if i % 20 == 0 and i != max_tab:
                    cont = input("Continuar tabuada? (s/n): ")
                    if cont.lower() != "s":
                        break
            if i != max_tab:
                break
