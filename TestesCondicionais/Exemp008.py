'''
Crie um programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido
'''

sexo = str(input('Informe seu sexo escreva, F - Feminino, M - Masculino: '))
if sexo == "F":
    print('Sexo Feminino!')
else:
    if sexo == "M":
        print('Sexo Masculino')
    else:
        print('Sexo Inválido')
