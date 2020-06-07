'''
 Faça um programa, com uma função que necessite de três argumentos, e
que forneça a soma desses três argumentos através de uma função. Seu
script também deve fornecer a média dos três números, através de uma
segunda função que chama a primeira.
'''
# def soma
def soma(x,y,z):
    res = x + y + z
    return res
# def media
def media(x,y,z):
    #som = soma(x,y,z)
    med = soma(x,y,z)/3
    return med
# função com três argumentos
def menu():
    x = int(input('Primeiro numero: '))
    y = int(input('Segundo numero : '))
    z = int(input('Terceiro numero: '))

    print('Soma: ', soma(x,y,z))
    print('Media:', media(x,y,z))

while True:
    menu()

