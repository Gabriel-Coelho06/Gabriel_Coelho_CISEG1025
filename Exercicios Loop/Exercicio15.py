for i in range(0, 256, 20):
    for j in range(i, min(i+20, 256)):
        print(j, chr(j))
    if i + 20 < 256:
        continuar = input("Continuar? (s/n): ")
        if continuar.lower() != "s":
            break
