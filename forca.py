print("Bem vindo ao jogo da forca!!")

palavra_secreta = "Mouse".upper()
letras_acertadas = ["_" for letra in palavra_secreta]

print(letras_acertadas)

enforcou = False
acertou = False
erros = 0

while enforcou == False and acertou == False:
    chute = input("Digite uma letra: ")
    chute = chute.strip().upper()

    if chute in palavra_secreta:
        indice = 0
        for letra in palavra_secreta:
            if chute == letra:
                letras_acertadas[indice] = letra
            indice += 1
            if "_" not in letras_acertadas:
                acertou = True
                print("Voce venceu!!")
    if chute == palavra_secreta:
        acertou =  True
        
        letras_acertadas = palavra_secreta
        print("Voce acertou a palavra!")           
    else:
        erros += 1
        print("Número de erros: ", erros)

        if erros == 15:
            enforcou = True
            print("Voce perdeu :(")
            print("A palavra correta era: ", palavra_secreta)
    

    print(letras_acertadas)
