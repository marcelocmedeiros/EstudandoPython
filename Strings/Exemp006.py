''' String toda em maiúscula ou minúscula: isupper() e islower() '''

"""
Crie um script que peça uma string ao usuário e diga se:
    Ela é toda maiúscula
    Ela é toda minúscula
    Tem caracteres maiúsculos e minúsculos
"""

while True:
    texto = input("Digite uma string: ")
    if texto.isupper():
        print("Tudo maiusculo")
    elif texto.islower():
        print("Tudo minusculo")
    else:
        print("Misturado")
# ver outros exemplos abaixo

"""texto = "MARCELO"
print(texto.isupper())

texto = "MARCELO"
print(texto.islower())

texto = "marcelo"
print(texto.islower())

texto = "Marcelo"
print(texto.islower())
"""