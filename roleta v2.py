import random
balasescolhidas=[]
points=0
cont=1
def reiniciar():
    points=int(0)
def roleta():
    cont=int(1)
    roletarussa=[1,2,3,4,5,6]
    maximo=[1,2,3]
    numerodevivas=random.choice(maximo)
    for i in range(numerodevivas):
        balasescolhidas.append(int(roletarussa[i]))
    for i in range(numerodevivas):
        balas=random.choice(roletarussa)
    print(f"Existem {numerodevivas} balas reais na arma, todas as outras {6-numerodevivas} são falsa")
    atirar(cont, points)

def morte():
    print("O seu total de pontos é", points)
    escolha2=str(input("Deseja continuar? (Responda sim ou não)"))
    if escolha2=="sim":
        points=int(0)
        reiniciar(points)
        roleta()
    elif escolha2=="não":
        print("Obrigado por jogar!")

def atirar(cont, points):
    escolha=str(input("Você deseja atirar? (Responda sim ou não)"))
    if escolha=="sim":
        for i in range(1,7):
            if cont==balasescolhidas[i]:
                print("Você morreu")
                morte(points)
            else:
                print("Você continua vivo +10 pontos")
                points = points+0
                roleta()
    elif escolha=="não":
        cont=1+cont
        if cont>6:
            print("Você não atirou nenhuma vez, retorna à primeira bala")
            cont=1
        atirar(cont, points)
roleta()