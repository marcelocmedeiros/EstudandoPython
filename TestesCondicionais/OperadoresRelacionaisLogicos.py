# A instrução if é uma condição representa uma comparação ou um conjunto de comparações que irá resultar sempre em um valor do tipo lógico (boolean), isto é, VERDADEIRO (True) ou FALSO (False). 
# Operadores relacionais – são os seguintes:
"""
    • x == y        # o valor de x é igual ao de y?
    • x != y        # o valor de x é diferente do valor de y?
    • x > y         # o valor de x é maior que o de y?
    • x < y         # o valor de x é menor que o de y?
    • x >= y        # o valor de x é maior ou igual ao de y?
    • x <= y        # o valor de x é menor ou igual ao de y?
    • x is y
    • x is not y    # x e y apontam/não apontam para o mesmo
    endereço de memória?
"""

# Operadores lógicos:
"""
    • and       # a sentença é verdadeira se TODAS as condições forem verdadeiras
    • or        # a sentença é verdadeira se UMA das condições for verdadeira
    • not       # inverte o valor lógico de uma sentença (True → False, False → True)
"""
# Operadores relacionais e lógicos

print('* * * * parte 1 * * * * ')
print()

print(4 * 2 == 8) #True.
print(9 ** 2 == 81) #True.
print(5 + 2 < 7) #False.
print(5 + 2 >= 7) #True.
print('Portela' == 'Mangueira') #False.
print(5 / 2 > 3) #False.
print(7 % 2 != 0) #True.

print('\n\n* * * * parte 2 * * * * ')
print()

pais = 'Brasil'
print(pais == 'Brasil') #True.
print(pais == 'BRASIL') #False.
media_final = 7.0
if (media_final >= 7.0):
    print('com a média', media_final, 'você está aprovado')
else:
    print('reprovado')
a=10; b=100
if (a >= b):
    print('o valor de "a" é maior ou igual ao de "b"')
else:
    print('o valor de "a" é menor do que o de "b"')

print('\n\n* * * * parte 3 * * * * ')
print()

print((4 * 2 == 8) and (9**2 >= 81)) #True.
print((1 + 1 < 3) and (9**2 > 81)) #False.
print((1 + 1 < 3) or ('cruzeiro' == 'atletico')) #True.