# Como Mudar a Key (Chave) de um Dicionário
'''
não é permitido mudar uma Key.
mas podemos copiarmos o seu value para colocarmos ele em uma nova chave, com novo nome.
'''
# Maneira 1 de mudar a key

notas={'João' : 9,
'Maria' : 10,
'José' : 4 }
print(notas)
# 1° Marya recebe as notas de Maria
notas['Marya'] = notas['Maria']
# depois deletamos Maria do dic
del notas['Maria']
print(notas)

# Maneira 2 de alterar a key

notas={'João' : 9,
'Maria' : 10,
'José' : 4 }
print(notas)
# aqui atribuimos as notas de maria p marya e deletamos maria na mesma linha usando pop()
notas['Marya'] = notas.pop('Maria')
print(notas)
