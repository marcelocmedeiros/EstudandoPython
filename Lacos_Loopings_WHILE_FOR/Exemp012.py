'''
Crie um script em Python que pede qual tabuada o usuário quer ver, em seguida imprima essa tabuada
'''

tabuada = int(input('Qual tabuada quer fazer:'))

for var in range(1, 11):
    print(tabuada,'x',var, '=', tabuada*var)

