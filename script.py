import random

print("**********************************")
print("Bem vindo ao jogo de adivinhação!!")
print("**********************************")

secNum = random.randrange(1,1000)
tentativas = 0
pontos = 1000
pontosP = 0
rodada = 0


print("Qual nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")


nivel = int(input("Defina o nível: "))

while (nivel > 3 or nivel < 1):
    print("Digite um valor entre 1 e 3")
    nivel = int(input("Defina o nível: "))

if(nivel == 1):
    tentativas = 30
    pontosP = 25
elif (nivel == 2):
    tentativas = 20
    pontosP = 50
elif (nivel == 3):
    tentativas = 10
    pontosP = 100


for rodada in range(tentativas):
    print("\nTentativa ", rodada, "de ", tentativas)
    chute = int(input("Digite um número entre 1 e 1000: "))
    print("\nVocê digitou", chute)

    if (chute> 1000 or chute<1):
        print("Você deve digitar um número entre 1 e 1000!")
        continue

    acertou = bool(chute == secNum)
    maior = bool(chute > secNum)
    menor = bool(chute < secNum)

    if (acertou == True):
        print("Você acertou e fez {} pontos!".format(pontos))
        print("Você usou {} tentativas!".format(rodada))
        break
    else:
        pontos = pontos-pontosP
        rodada += 1
        if(maior):
            print("Errado, seu chute foi maior do que o número secreto.")
        elif(menor):
            print("Errado, seu chute foi menor do que o número secreto.")

if (rodada == tentativas):
    print("O número secreto era {}".format(secNum))
    print("Você usou {} tentativas!".format(rodada))

print("Fim do Jogo!")
input()