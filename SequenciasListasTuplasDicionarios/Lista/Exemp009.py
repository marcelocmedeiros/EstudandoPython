# Operações com Listas:
"""
•inverter uma lista: reverse()
•embaralhar uma lista: sort()
•apagar uma lista: clear()
•copiar uma lista: copy()
•contar quantas vezes um determinado item  aparece: count(x)
•retirar um elemento específico da linha: pop(x)
"""

numeros = [14.55, 67, 90, 10, 21]
# Valores mínimos, máximos e soma
print(min(numeros), max(numeros), sum(numeros))

#Verificando a existência de itens em uma lista
lista = ['O carro azul', 'peixe', 'O carro azul','peixe',  'O carro azul', 'peixe']

print('peixe' in lista)
print('gato' in lista)

# método insert() que, além do elemento a ser inserido, recebe também o índice que ele deve assumir
livros = ['Java', 'SqlServer', 'Delphi', 'Python', 'Android']
livros.insert(0,'Oracle')
print(livros)


livros1 = ['Java', 'SqlServer', 'Delphi', 'Python', 'Android','Java']
#contar quantas vezes um determinado item  aparece: count(x)
livros1.count('Java')
print('count()',livros.count('Java'))
# sort() embaralhar uma lista
livros1.sort()
print('sort()',livros1)
#inverter uma lista: reverse()
livros1.reverse()
print('reverse()',livros1)
# método pop(), por padrão remove o último item da lista. Caso seja necessário remover um índice específico
livros1.pop()
print(livros1)
livros1.pop(1)
print(livros1)
#o método remove(item) remover o item a partir do seu valor
livros1.remove('Delphi')
print(livros1)
# apagar uma lista: clear()
livros1.clear()
print('clear',livros1)
#









