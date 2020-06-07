'''
A probabilidade de dar um valor em um dado é 1/6 (uma em 6). Faça um
script em Python que simule 1 milhão de lançamentos de dados e mostre a
frequência que deu para cada número.
'''
# importando biblioteca random gera número aleatorios
import random

def gera():
    return random.randint(1,6)


def repete(n):
    test1 = test2 = test3 = test4 = test5 = test6 = 0

    # laço for pra rodar n vezes o lançamento de dados
    for val in range(n):
        # Cada vez que lança o dado chamando a função gera() armazenamos na variável test
        test = gera()
        #vamos fazer várias comparações com IF, ELIF e ELSE, para saber se o valor do dado é 1, 2, 3, 4, 5 ou 6.
        # E quando achar o valor certo, incrementar em 1 o valor da variável
        if(test==1):
            test1 += 1
        elif(test==2):
            test2 += 1
        elif(test==3):
            test3 += 1
        elif(test==4):
            test4 += 1
        elif(test==5):
            test5 += 1
        else:
            test6 += 1


    print("Numero 1 saiu ", test1," vezes = ",(test1/n)*100, " %")
    print("Numero 2 saiu ", test2," vezes = ",(test2/n)*100, " %")
    print("Numero 3 saiu ", test3," vezes = ",(test3/n)*100, " %")
    print("Numero 4 saiu ", test4," vezes = ",(test4/n)*100, " %")
    print("Numero 5 saiu ", test5," vezes = ",(test5/n)*100, " %")
    print("Numero 6 saiu ", test6," vezes = ",(test6/n)*100, " %")

def menu():
    n = int(input('Quantos lançamentos de dado? '))
    repete(n)


while True:
    menu()