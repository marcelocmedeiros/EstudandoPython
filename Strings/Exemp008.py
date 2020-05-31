''' sdecimal() retorna True se tudo for número'''

while True:
    texto = input("Digite uma string: ")
    if texto.isalpha():
        print("Tudo tudo letra")
    elif texto.isdecimal():
        print("Tudo numero")
    else:
        print("Misturado, vazio ou caractere especial")

# outros exemplos
'''texto = "marcelo42"
print(texto.isdecimal(),'\n')
texto1 = "12345"
print(texto1.isdecimal())'''