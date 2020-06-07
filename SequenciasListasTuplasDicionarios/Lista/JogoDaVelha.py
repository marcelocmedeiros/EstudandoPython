# Lógica do jogo da velha

#Código Python do Jogo da Velha

def menu():# função menu()
    # var = 1 p while continuar perguntando
    continuar=1
    while continuar:
        # caso usuario digite 0 sair
        continuar = int(input("0. Sair \n"+
    "1. Jogar novamente\n"))
    if continuar:
        game()
    else:
        print("Saindo...")

def game():# função que vai controlar o jogo
    jogada=0 # contar o n° de jogadas
    while ganhou() == 0:
        # jogada%2 + 1, aqui controla qual jogador vai jogar 1 ou 2
        print("\nJogador ", jogada%2 + 1)
        exibe() # exibimos o tabuleiro
        # pede em q local quer jogar (linha, coluna)
        linha = int(input("\nLinha :"))
        coluna = int(input("Coluna:"))

        if board[linha-1][coluna-1] == 0: # testa se o lendereço está vazio
            if(jogada%2+1)==1: # se True então verifica quem jogou 
                board[linha-1][coluna-1]=1 # X para jogador 1
            else:
                board[linha-1][coluna-1]=-1 # O para jogador -1
        else:
            print("Não esta vazio") # se False informa 
            jogada -=1 # retiramos um da var jogada não não soma essa jogada
        if ganhou(): # verificamos se ganhou chamando função ganhou
            print("Jogador ",jogada%2 + 1," ganhou apos ", jogada+1," rodadas")
        jogada +=1 # soma +1 jogada correta
def ganhou():
    #checando linhas
    for i in range(3):
        soma = board[i][0]+board[i][1]+board[i][2]
        if soma==3 or soma ==-3:
            return 1 # retorna 1 quando soma == 3 ou -3 jogo acaba ganhou
    #checando colunas
    for i in range(3):
        soma = board[0][i]+board[1][i]+board[2][i]
        if soma==3 or soma ==-3:
            return 1 # retorna 1 quando soma == 3 ou -3 jogo acaba ganhou
    #checando diagonais
    diagonal1 = board[0][0]+board[1][1]+board[2][2]
    diagonal2 = board[0][2]+board[1][1]+board[2][0]
    if diagonal1==3 or diagonal1==-3 or diagonal2==3 or diagonal2==-3:
        return 1 # retorna 1 quando soma == 3 ou -3 jogo acaba ganhou
    return 0 # retorna 0 quando soma != 3 ou -3 jogo continua
    # imprime o tabuleiro
def exibe():
    # um laçofor dentro de outro for
    for i in range(3): # exibi a linha
        for j in range(3): # exibi a coluna
            if board[i][j] == 0: 
                print(" _ ", end=' ') # exibi "_" para preencher (X ou O)
            elif board[i][j] == 1:# quando for 1
                print(" X ", end=' ') # exibi X
            elif board[i][j] == -1:# quando for -1
                print(" O ", end=' ')# exibi O
    print()
# inicialmente a matriz toda 0
board= [ [0,0,0],
[0,0,0],
[0,0,0] ]
# chamndo o jogo
menu()