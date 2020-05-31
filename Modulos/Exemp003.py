'''
randrange()
A função randrange é bem similar a função range, exatamente a mesma maneira de se usar os
parâmetros, a diferença que ela vai retornar apenas um valor.
'''
from random import randrange
# randrange(x) - vai gerar um número aleatório de 0 até x-1

#Pode retornar:0, 1, 2, 3 ou 4
print(randrange(5))
#Dois argumentos: randrange(x,y) - vai gerar um número de x até y-1

#Pode sair:1, 2, 3 ou 4
print(randrange(1,5))
#Três argumentos: randrange(x,y,z) - Pode gerar de x até y-1, mas ao invés de 1 em 1, ela 'pula' de z em z, ou seja, z é o salto.

#Vai gerar uma dos seguintes números: 0, 2, 4, 6 ou 8 (ou seja, todos os pares de 0 até 8)
print(randrange(0,10,2))

#Para gerar todos os números múltiplos de 3 menores que 100, fazemos: randrange(0, 101, 3) : 3, 6, 9, ..., 99
print(randrange(0,101,3))