'''
Use exemplo anterior caso o usuário digite:
Fala galera, meu numero é 1234-5678
'''

def eTelefone(numero):
    # verifica se tem 9 caracteres
    if len(numero) != 9:
        return False
    # um laço nos 4 primeiros indices
    for index in range(0,4):
        # verifica se dentro da lista [index] é tudo número
        if numero[index].isdecimal() is not True:
            return False
    # verifica se o 4° indice é == "-"
    if numero[4] != '-':
        return False
    # um laço nos 4 últimos indices
    for index in range(5,9):
        # verifica se dentro da lista [index] é tudo número
        if numero[index].isdecimal() is not True:
            return False
    print("Numero detectado: ", numero)
    return True

while True:
    numero = input("Numero no formato 'xxxx-yyyy': " )
    # percorre todos elementos de numero
    for i in range( len(numero)):
        # analisar blocos de 9 caracteres, 9 em 9 | pedaco[i:i+9]
        pedaco=numero[i:i+9]
        # chamando a def por pedaços fatiados acima
        eTelefone(pedaco)