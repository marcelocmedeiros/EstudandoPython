di = {'Julio': 'C', 'Jaime': 'Python', 'Ana': 'Ruby', 'Cláudia': 'Java'}
y = di['Ana']
print(y)
x = di['Julio']
print(x)
linguagem = di.get('Ana')
print(linguagem)

# Percorrendo dicionários com for

linguagens =  {'Julio': 'C', 'Jaime': 'Python', 'Ana': 'Ruby', 'Cláudia': 'Java', 'Mauro': 'PHP'}
for chave in linguagens:
    print(chave, 'programa em:', linguagens[chave])

# Alterando um valor em um dicionário

m = di['Jaime']
print(m)
di['Jaime'] = 'PHP'
n = di['Jaime']
print(n)

# Inserindo um item em um dicionário

di['Marcelo'] = 'HTML5'
print(di)

# Inserindo itens ou alterando itens em um dicionário com o método update()

# sintaxe di.update(t) onde di e t são dicionários e cada par chave, valor de t é adicionado a di

di.update({'Paulo': 'C++', 'Mauro': 'Swift'})
print(di)

# Removendo um par chave, valor de um dicionário usando o comando del

del di['Mauro']
print(di)

# Removendo e obtendo um par chave, valor com o método pop()

v = di.pop('Jaime')
print(v)
print(di)
# adicionar um parâmetro extra pop(k, v) onde o parâmetro extra substitui o valor retornado caso a chave k não conste do dicionário

v = di.pop('Carlos', 'Não existe')
print(v)
print(di)

# Visualizações de dicionários
'''
método	            descrição
keys()	  -->      Retorna uma visualização de todas as chaves de um dicionário.
values()  -->      Retorna uma visualização de todas os valores de um dicionário.
items()	  -->      Retorna uma visualização de todos pares (chave, valor) de um dicionário.
'''

k = di.keys()
print(k)
v = di.values()
print(v)
i = di.items()
print(i)

# Visualizações são iteráveis

x = di.items()
print(x)
for k, v in x:
    print('chave:', k, end = ", ")
    print('valor:', v)
# gerarando listas ou tuplas

x = di.keys()
y = di.values()
li = list(x)
ly = list(y)
print('='*6,'Listas','='*6)
print('Listas das Keys:',li)
print('Listas das Valous:',ly)
tu = tuple(x)
ty = tuple(y)
print('='*6,'Tuplas','='*6)
print('Tuplas das Keys:',tu)
print('Tuplas das Valous:',ty)
