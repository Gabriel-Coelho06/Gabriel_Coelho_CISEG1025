clientes = []
id_auto = 1

def calcular_desconto(compra):
    if 100 <= compra <= 200:
        return 0.05
    elif 200 < compra < 500:
        return 0.10
    elif compra >= 500:
        return 0.15
    else:
        return 0

while True:
    print("\nMenu Clientes:")
    print("1 - Inserir cliente")
    print("2 - Listar clientes")
    print("3 - Buscar cliente por numero")
    print("4 - Sair")
    
    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        nome = input("Nome do cliente: ").strip()
        while not nome:
            nome = input("Nome invalido. Digite novamente: ").strip()

        morada = input("Morada: ").strip()
        while not morada:
            morada = input("Morada invalida. Digite novamente: ").strip()

        tel = input("Telemovel: ").strip()
        while not tel.isdigit():
            tel = input("Telefone invalido. Digite apenas numeros: ").strip()

        nif = input("NIF: ").strip()
        while not nif.isdigit():
            nif = input("NIF invalido. Digite apenas numeros: ").strip()

        while True:
            try:
                compra = float(input("Valor da compra: "))
                if compra < 0:
                    print("Compra nao pode ser negativa")
                    continue
                break
            except:
                print("Entrada invalida, digite um numero")

        desconto = calcular_desconto(compra)
        divfinal = compra - (compra * desconto)

        clientes.append({
            "NumCli": id_auto,
            "NomCli": nome,
            "Morada": morada,
            "Tel": tel,
            "NIF": nif,
            "Compra": compra,
            "Desconto": desconto*100,  # percentual
            "DivFin": divfinal
        })
        print(f"Cliente inserido com Numero: {id_auto}")
        id_auto += 1

    elif opcao == "2":
        if not clientes:
            print("Nenhum cliente cadastrado")
            continue
        idx = 0
        while idx < len(clientes):
            c = clientes[idx]
            print("\n------------------------")
            print("Numero do Cliente:", c["NumCli"])
            print("Nome:", c["NomCli"])
            print("Morada:", c["Morada"])
            print("Tel:", c["Tel"])
            print("NIF:", c["NIF"])
            print("Valor da Compra:", c["Compra"])
            print("Desconto aplicado (%):", c["Desconto"])
            print("Divida Final:", c["DivFin"])
            print("------------------------")
            idx += 1
            if idx < len(clientes):
                cont = input("Continuar listagem? (enter para sim, n para parar): ")
                if cont.lower() == "n":
                    break

    elif opcao == "3":
        if not clientes:
            print("Nenhum cliente cadastrado")
            continue
        while True:
            try:
                num = int(input("Digite o numero do cliente: "))
                break
            except:
                print("Entrada invalida, digite um numero")

        encontrado = False
        for c in clientes:
            if c["NumCli"] == num:
                print("\n------------------------")
                print("Numero do Cliente:", c["NumCli"])
                print("Nome:", c["NomCli"])
                print("Morada:", c["Morada"])
                print("Tel:", c["Tel"])
                print("NIF:", c["NIF"])
                print("Valor da Compra:", c["Compra"])
                print("Desconto aplicado (%):", c["Desconto"])
                print("Divida Final:", c["DivFin"])
                print("------------------------")
                encontrado = True
                break
        if not encontrado:
            print("Cliente nao encontrado")

    elif opcao == "4":
        print("A Sair!")
        break
    else:
        print("Opcao invalida. Tente novamente.")
