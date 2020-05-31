'''
Faça um programa em Python que solicite um número positivo inteiro ao
usuário, e depois exiba um tabuleiro na tela, com igual número de linhas e
colunas
'''

print("Vamos criar um tabuleiro de tamanho: N x N")

n=int(input("Valor de N: ") )
# laço FOR vai ser responsável por percorrer as linhas
for linha in range(n):
    for coluna in range(n):
        #cada linha dessa, precisamos desenhar as colunas, onde cada coluna printamos um "x "
        print("x ",end='')# adicionar o end='' na função print, p não pular de linha
    # Quando terminar de imprimir cada linha print() para dar uma quebra de linha
    print()