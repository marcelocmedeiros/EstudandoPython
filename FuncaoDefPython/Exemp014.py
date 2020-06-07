# return com strings
# def com 2 parametros
def inverte(nome, sobrenome):
    # variével q inverte a string
    nomeInverso = sobrenome+", "+nome
    # retorna para variável invertido o valor de nomeInverso
    return nomeInverso

# programa principal
nome = input("Nome: ")
sobrenome = input("Sobrenome: ")
# chamo a def
invertido = inverte(nome,sobrenome)
print("Olá", invertido)