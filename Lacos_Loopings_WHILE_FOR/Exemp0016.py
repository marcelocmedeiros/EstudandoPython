'''
Crie um programa em Python que pede um número inteiro ao usuário e calcule seu fatorial
'''
# usando For

num = int(input('Digite um número inteiro:'))
# variável acumulativa
fatorial= 1
# não esquecer ranger (1 até num -1), para usar num tenho que soma +1
for var in range(1, num+1):
    # aqui fatorial vai se multiplicar a cada laço 1x1, 1x2,1x3...1xnum
    fatorial*=var

print(fatorial)