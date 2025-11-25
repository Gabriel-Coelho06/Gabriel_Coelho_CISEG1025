n = int(input("Introduza um numero: "))

if n < 2:
    print("Nao e primo")
else:
    primo = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            primo = False
            break

    if primo:
        print("E primo")
    else:
        print("Nao e primo")
