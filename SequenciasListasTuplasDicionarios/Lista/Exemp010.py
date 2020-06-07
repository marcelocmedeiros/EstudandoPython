# O Laço FOR com Listas em Python
'''
Faça um script que cria uma lista de 10 elementos, preenchendo eles de 0
até 9, usando laço for. Depois, printe essa lista.
'''

numeros = []

for count in range(10):
    #concatenamos o valor a lista numeros
    numeros += [count]

print(numeros)