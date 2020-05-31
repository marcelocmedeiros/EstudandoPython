'''
Crie uma função que recebe um inteiro positivo e teste para saber se ele é
primo ou não. Faça um script que recebe um inteiro n e mostra todos os
primos, de 1 até n.
'''

# def primo
def primo(x):
    # código para saber se é primo
    for val in range(2, x):
        # vai testa a divisão apartir de 2 até o número "n" informado se tem divisão == 0
        if x % val == 0:
            return False
    return True

def menu():
    x = int(input('Digite um número inteiro positivo: '))
    for val in range(2, x + 1):
        if (primo(val)):
            print(val, end=', ')
    print()


while True:
    menu()