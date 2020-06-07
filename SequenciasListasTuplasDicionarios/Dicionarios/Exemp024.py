# Como Exibir Dicionários

"""
1. Método items(): exibe todos os itens, ou seja, os pares chave-valor
2. Método keys(): exibe todas as chaves de um dicionário
3. Método values(): exibe todos os valores de um dicionário
"""

# Como exibir os items: Método items()

notas={'joao' : 9,
'maria' : 10,
'zezinho': 4}
print( notas.items() )

#Com exibir chaves de um dicionário: Método keys()

notas={'joao' : 9,
'maria' : 10,
'zezinho': 4}
print("Exibindo chaves:")
print( notas.keys() )

# Como exibir valores de um dicionário: Método values()

notas={'joao' : 9,
'maria' : 10,
'zezinho': 4}
print("Exibindo valores:")
print( notas.values() )