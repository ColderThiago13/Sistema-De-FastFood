print("Bem vindo ao Sistema Movie Theater !!")

listaFilmes = []

totalIngressos = 10

ingresso = 0

saiu = False

while saiu == False:
    print("1. Adicionar filme")
    print("2. Remover filme")
    print("3. Buscar filme")
    print("4. Editar filme")
    print("5. Vender ingresso")
    print("6. Sair")

    opcao = int(input("Digite sua opção: "))

    if opcao == 1:
        print("Qual filme deseja adicionar? ")
        filme = input().upper().strip()
        listaFilmes.append(filme)

    if opcao == 2:
        print("Qual filme deseja remover? ")
        filme = input().upper().strip()
        listaFilmes.remove(filme)
    if opcao == 3:
        print("Qual filme deseja buscar? ")
        filme = input().upper().strip()
        if filme in listaFilmes:
            posicaoLista = listaFilmes.index(filme)
            print(listaFilmes[posicaoLista])
        else:
            print("Filme ", filme, " não foi encontrado.")
    if opcao == 4:
        print("Qual filme deseja substituir? ")
        filme = input().upper().strip()
        if filme in listaFilmes:
            posicaoLista = listaFilmes.index(filme)

            print(filme, " sera substituido por: ")

            novoFilme = input().upper().strip()
            listaFilmes[posicaoLista] = novoFilme

            print(filme, " foi substituido por: ", novoFilme)
        else:
            print("Filme ", filme, " não foi encontrado.")
    if opcao == 5:
        print("Quantos ingressos você deseja vender?")
        qtdIngresso = int(input())
        if (qtdIngresso + ingresso) <= totalIngressos:
            print("Ingressos vendidos")
            ingresso += qtdIngresso
        else:
            print("Você só pode vender 10 ingressos no total!!! \n", "Você ja vendeu: ", ingresso)

    if opcao == 6:
        print("Encerrando programa...")
        saiu = True
    
    if (listaFilmes == []):
        print("Não há nenhum filme na lista.")
    else:
        print(listaFilmes)
        