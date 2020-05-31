'''
Crie um script em Python que gere 6 números aleatórios para a Mega-Sena
(neste jogo, você pode escolher dezenas de 1 até 60). Não pode repetir
dezena.
'''
from random import sample
"""retorna uma lista específica de itens escolhidos da sequência, ou seja, lista, tupla, 
string ou conjunto. Usado para amostragem aleatória sem substituição."""

def megasena():
    # sorteio de 6 n° entre (1,61) sem repetição
    n1 = sample(range(1,61),6)
    return n1


megasena()
print('jogo: ',megasena())

