import random
i=int()
ndebalasreais=int()
points=int(0)
cont=int(1)
balasescolhidas=[]
def escolhimento(escolha,cont):
    if escolha=="sim":
        for i in range(ndebalasreais):
            if cont==balasescolhidas[i]:
                morte()
            else:
                print("Você continua vivo +10 pontos")
                points=points+10
    elif escolha=="não":
        print("Você foi para a próxima bala")
        cont=cont+1
        atirar()
    else:
        print("Não entendi, pode repetir?")
        atirar(ndebalasreais,cont,balasescolhidas)
def morte(points):
    print(f"Você morreu seu total de pontos foi de {points}")
    print("Você gostaria de reiniciar?")
    escolhas=str(input(""))
    if escolhas=="sim":
        reiniciar()
    elif escolhas=="não":
        print("Obrigado por jogar")
    else:
        print("Não entendi")
        morte()
def reiniciar():
    points=0
    roleta(points)
def atirar(ndebalasreais, cont, balasescolhidas):
    print("Você deseja atirar?")
    escolha=str(input(""))
    escolhimento(escolha,cont)
    if cont>6:
        print("Você já passou da sexta bala, retornando à primeira")
        cont=1
        atirar()
def roleta(ndebalasreais,cont,balasescolhidas,i):
    balasescolhidas=[]
    cont=1
    rr=[1,2,3,4,5,6]
    maximo=[1,2,3]
    ndebalasreais=random.choice(maximo)
    for i in range(ndebalasreais):
        balasescolhidas.append(random.choice(rr))
    print(f"Existem {ndebalasreais} balas reais na arma, todas as outras são falsas")
    atirar(ndebalasreais,cont,balasescolhidas)
print("Responda todas as perguntas apenas com sim ou não.")
roleta(ndebalasreais,cont,balasescolhidas,i)