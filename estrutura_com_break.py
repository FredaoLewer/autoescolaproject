while True:
    opcao = int(input("Informe um numero: "))

    if opcao == 101:
        break

    print (opcao)

    for numero in range(100):

        if numero == 15:
            break
        print(numero, end=" ")
        