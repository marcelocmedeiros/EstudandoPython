''' método isalpha() retorna True se todas as letras de uma string forem letras'''

while True:
    texto = input("Digite uma string: ")
    if texto.isalpha():
        print("Tudo letra")
    else:
        print("Nem tudo é letra")

# outros exemplos
"""texto = "marcelo42"
print(texto.isalpha(),'\n')
texto1 = "marcelo"
print(texto1.isalpha())"""