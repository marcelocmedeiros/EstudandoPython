'''
isspace() só retorna True se tivermos espaço em branco, tabulação
ou quebra de linha.
Retorna False caso contrário ou a string seja vazia
'''

while True:
    texto = input("Digite uma string: ")
    if texto.isalpha():
        print("Tudo tudo letra")
    elif texto.isdecimal():
        print("Tudo numero")
    elif texto.isalnum():
        print("Numeros e letras")
    elif texto.isspace():
        print("Composto so de espaço, e/ou tabulação e/ou quebra de linha")
    else:
        print("Vazia ou caractere especial")


