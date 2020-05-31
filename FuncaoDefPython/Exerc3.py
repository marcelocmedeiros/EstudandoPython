'''
Faça um programa que recebe três números do usuário, e identifica o
maior através de uma função e o menor número através de outra função.
'''

# def maior
def maior(x,y,z):
    if x>y and x>z:
        mai = x
    elif y>x and y>z:
        mai = y
    else:
        mai = z
    return mai
# def menor
def menor(x,y,z):
    if x < y and x < z:
        men = x
    elif y < x and y < z:
        men = y
    else:
        men = z
    return men
# função com três argumentos
def menu():
    x = int(input('Primeiro numero: '))
    y = int(input('Segundo numero : '))
    z = int(input('Terceiro numero: '))

    print('Soma: ', maior(x,y,z))
    print('Media:', menor(x,y,z))

while True:
    menu()
