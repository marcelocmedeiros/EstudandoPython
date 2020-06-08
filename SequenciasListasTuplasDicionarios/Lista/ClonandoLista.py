# Suponha que você tenha uma lista “a” e queira gerar uma cópia da mesma em uma outra lista “b”. Nesta situação, você não deve utilizar de jeito nenhum o comando abaixo:
# b = a
# Isso não resultará na criação de um novo objeto; na verdade, a atribuição criará apenas uma nova variável que faz uma referência ao objeto original. Esse processo é chamado de cópia rasa

# Parase obter uma cópia profunda (deep copy), que consiste em criar uma cópia real ou um clone de um objeto. Existem duas formas:

'''
• Fatiamento: a operação de fatiamento de listas sempre gera clones (ou seja, as sublistas geradas são sempre cópias reais dos dados de uma lista). Desta forma, utilizando o comando b = a[:] você consegue obter uma sublista que na verdade é uma cópia completa da lista original.

• Módulo ‘copy’: oferece uma função chamada deepcopy() para realizar a cópia profunda não apenas de listas, mas de qualquer objeto complexo: b = copy.deepcopy(a).
'''
# Realizando a cópia rasa e a clonagem de listas.
# Shallow copy (referência) x deep copy (clonagem)

import copy
#1-Shallow Copy
print('* * SHALLOW COPY')
a = [1,2,3,4,5]
b = a
print('-a=',a)
print('-b=',b)
b[0] = 999
print('\t-a',a)
print('\t-b:',b)
print('\t-a is b?',a is b) #True (o operador "is" verifica se dois objetos têm a mesma referência)
print('\n-------------------------------------')

#2-Deep Copy utilizando a técnica de fatiamento
print('* * DEEP COPY COM FATIAMENTO')
c = [1,2,3,4,5]
d = c[:]
print('-c=',c)
print('-d=',d)
d[0] = 999
print('\t-c:',c)
print('\t-d:',d)
print('\t-c is d?',c is d) #False
print('\n-------------------------------------')

#3-Deep Copy utilizando o módulo ‘copy’
print('* * DEEP COPY COM O MÓDULO \'copy\'')
e = copy.deepcopy(c)
print('-c=',c)
print('-e=',e)
e[0] = 999
print('\t-c:',c)
print('\t-e:',e)
print('\t-a is b?',c is d) #False