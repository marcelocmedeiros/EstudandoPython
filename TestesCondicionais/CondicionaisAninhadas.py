# Condicionais Aninhadas
 # Quando houver um IF dentro de outro IF ou IF dentro do ELSE

a = int(input('Informe o 1º número: '))
b = int(input('Informe o 2º número: '))
if (a == b):
    print("a e b são iguais")
else:
    if (a > b):
        print("'A' é maior do que 'B'")
    else:
        print("'A' é menor do que 'B'")