# Assim como ocorre com as tuplas, as strings são “imutáveis”, o que significa que não é possível alterar uma string existente. O máximo que se pode fazer é criar uma nova string que seja uma variação da original.


# Certo:
bicho='Capivara'
novo_bicho = 'K' + bicho[1:]
print(novo_bicho)

# Errado:
bicho='Capivara'
bicho[0] = 'K'
# TypeError: 'str' object does not support item assignment
print(bicho)