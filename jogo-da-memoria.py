import random

l1=random.sample([1,2,3,4],4)
l2=random.sample([5,6,7,8],4)
l3=random.sample([1,2,3,4],4)
l4=random.sample([5,6,7,8],4)

global mat 
mat=[]
list.append(mat,l1)
list.append(mat,l2)
list.append(mat,l3)
list.append(mat,l4)
random.shuffle(mat) #método que embaralha a ordem das listas.

global mat_oculta
mat_oculta = [['*','*','*','*'],['*','*','*','*'],['*','*','*','*'],['*','*','*','*']]

def imprime_matriz(m=mat_oculta):
    #função que printa uma matriz. Tem como argumento default a matriz inicial do jogo.
    for linhas in m:
        print(' ')
        for elementos in linhas:
            print(elementos, end = " ")

def atualiza_matriz(x,y):
    if(x>3 or y>3):
        print("Índices inválidos!")
        jogada()
    elif(mat_oculta[x][y]!='*'):
        print("Jogada inválida!")
        jogada()
    else:
        m1= mat[x][y]
        mat_oculta[x][y]=m1
        imprime_matriz(mat_oculta)
        
def jogada():
    #função que lê as tentativas do usuário
    
    jogada1=input("\nESCOLHA A PRIMEIRA JOGADA [X,Y]: ")
    x1=int(jogada1[1])
    y1=int(jogada1[3])
    atualiza_matriz(x1,y1)
    
    jogada2=input("\nESCOLHA A SEGUNDA JOGADA [X,Y]: ")
    x2=int(jogada2[1])
    y2=int(jogada2[3])
    atualiza_matriz(x2,y2)
    print('\n')
    teste(x1,y1,x2,y2)
 
def teste(x1,y1,x2,y2):
    # função que verifica se o usuário acertou a jogada
    if(mat[x1][y1]!=mat[x2][y2]):
        mat_oculta[x1][y1]='*'
        mat_oculta[x2][y2]='*'
        print("Voce errou! Tente de novo")
        imprime_matriz(mat_oculta)
                   
def main():
    print("JOGO DA MEMÓRIA:")
    imprime_matriz()
    while(mat_oculta!=mat):
        jogada()
    print("Você venceu!!")
    return

if __name__=="__main__":
    main()

