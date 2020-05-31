''' Separar e Quebrar Strings: split()'''

texto="Curso Python Progressivo"
# separa/quebra onde tem um espaço em branco retorna em uma lista
print( texto.split() )
print()
texto="123PI567PI9..."
# vai tira 'PI' da string e devolve uma lista com elementos separados onde antes era 'PI'
print( texto.split('PI') )
print()

