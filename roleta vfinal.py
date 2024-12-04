import random
i=str(123)
ndebalasreais=int()
points=int(0)
cont=int(1)
balasescolhidas=[]
def pontuação(points):
    points=points+10
    return points
def morte(points):
    print(f"Você morreu, seu total de pontos foi de {points}")
    print("Você gostaria de reiniciar?")
    escolhas=str(input(""))
    if escolhas=="sim":
        reiniciar(points)
    elif escolhas=="não":
        print("Obrigado por jogar")
        exit()
    else:
        print("Não entendi")
        morte(points)
def reiniciar(points):
    points=0
    roleta(points)
def atirar(ndebalasreais, cont, balasescolhidas, points, i):
    print("Você deseja atirar?")
    escolha=str(input(""))
    if escolha=="sim":
        for i in range(ndebalasreais):
            if cont==balasescolhidas[i]:
                morte(points)
            else:
                print("Você continua vivo +10 pontos")
                points = pontuação(points)
                roleta(points)
    elif escolha=="não":
        print("Você foi para a próxima bala")
        cont=cont+1
        atirar(ndebalasreais, cont, balasescolhidas, points, i)
    elif escolha=="suicidio":
        morte(points)
    elif escolha=="desistir":
        print("Obrigado por jogar! Você não ganhou nada.")
        exit()
    else:
        print("Não entendi, pode repetir?")
        atirar(ndebalasreais, cont, balasescolhidas, points, i)
    if cont>6:
        print("Você já passou da sexta bala, retornando à primeira")
        cont=1
        atirar(ndebalasreais, cont, balasescolhidas, points, i)
def roleta(points):
    balasescolhidas=[]
    cont=1
    rr=[1,2,3,4,5,6]
    maximo=[1,2,3]
    ndebalasreais=random.choice(maximo)
    for i in range(ndebalasreais):
        balasescolhidas.append(random.choice(rr))
    print(f"Existem {ndebalasreais} balas reais na arma, todas as outras são falsas")
    atirar(ndebalasreais,cont,balasescolhidas,points,i)
print("Responda todas as perguntas apenas com sim ou não.")
roleta(points)