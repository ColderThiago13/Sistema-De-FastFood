hamburguer = 10
batataFrita = 5
refrigerante = 4
sorvete = 2

print("[1] Hamburguer - R$", hamburguer)
print("[2] Batata Frita - R$", batataFrita)
print("[3] Refrigerante - R$", refrigerante)
print("[4] Sorvete - R$", batataFrita)

nome = str(input("Qual é o seu nome? \n"))
pedido = int(input("De 1 à 4, qual é o seu pedido? \n"))
qtd = int(input("Quantos você deseja? \n"))

print("O pedido de ", nome, " está a caminho.")

res = 0


if pedido == 1 :
    res = hamburguer * qtd
    tDeEspera = 5
if pedido == 2 :
    res = batataFrita * qtd
    tDeEspera = 3
if pedido == 3 :
    res = refrigerante * qtd
    tDeEspera = 0
if pedido == 4 :
    res = sorvete * qtd
    tDeEspera = 1

prazo = tDeEspera * qtd

if prazo >= 60 : 
    prazo = prazo/60



print("Preço: R$", res)
print("Prazo: ", prazo, "minutos")