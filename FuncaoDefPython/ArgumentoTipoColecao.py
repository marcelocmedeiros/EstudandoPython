# Programa que altera uma lista

def altera(li):
    for i in range(0, 3):
        li[i] = 'alterado'


lista = ['Paula', 'Raquel', 'Lucia', 'Ana', 'Maria']
print('Lista antes da função:')
print(lista)

altera(lista)
print()
print('Lista depois da função:')
print(lista)