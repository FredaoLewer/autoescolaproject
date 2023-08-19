idade = -1

while idade != 0:      #Enquanto for diferente de 0, as opções abaixo irão acontecer.
    print("Obrigado por utilizar nosso Sistema.")

    idade = int(input("Informe sua Idade: "))

    if idade <= 15:      #Se for igual a 17 anos.
        print("Você não está apto para as aulas Legislativas e nem para as aulas de Direção e começar o processo para tirar a sua CNH.")

    elif idade == 16 or 17 == idade:      #Se for igual a 16 ou 17 anos
        print("Parabéns, você está apto apenas para as aulas Legislativas, não podendo prosseguir para as aulas de Direção.")

    elif idade >= 18:      #Se for igual ou maior que 18 anos.
        print("Parabéns, você está apto para as aulas Legislativas e de Direção e começar o processo para tirar a sua CNH.")

else:
    print("Volte Sempre.")
    
