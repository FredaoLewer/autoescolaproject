print("Obrigado por utilizar nosso Sistema.")

opcao = int(input("Informe uma opção: [1] Insira sua Idade \n [2] Sair: "))

if opcao == 1:
    idade = int(input("Informe sua Idade: "))
    print(idade)

    if idade <= 15:      #Se for menor de 16 anos.
        print("Você não está apto para as aulas Legislativas e nem para as aulas de Direção e começar o processo para tirar a sua CNH.")

    elif idade == 16 or 17 == idade:      #Se for igual a 16 ou 17 anos.
        print("Parabéns, você está apto apenas para as aulas Legislativas, não podendo prosseguir para as aulas de Direção.")

    elif idade >= 18:      #Se for igual ou maior que 18 anos.
        print("Parabéns, você está apto para as aulas Legislativas e de Direção e começar o processo para tirar a sua CNH.")

else:
    print("Volte Sempre.")

if opcao == 2:
    quit  
