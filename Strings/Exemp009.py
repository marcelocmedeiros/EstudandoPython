'''
isalnum() retorna True se a string for um alfanumérico caso contrário, False.'''

while True:
    texto = input("Digite uma string: ")
    if texto.isalpha():
        print("Tudo tudo letra")
    elif texto.isdecimal():
        print("Tudo número")
    elif texto.isalnum():
        print("Números e letras")
    else:
        print("Vazia ou caractere especial")

# outros exemplos
"""texto = "marcelo42"
print(texto.isalnum(),'\n')
texto = "marcelo"
print(texto.isalnum(),'\n')
texto = "42"
print(texto.isalnum(),'\n')
texto1 = "m@r"
print(texto1.isalnum())
"""