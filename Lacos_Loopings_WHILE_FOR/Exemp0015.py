'''
Crie um programa em Python que pede um número inteiro ao usuário e calcule seu fatorial
'''
# usando While

num = int(input('Digite um número inteiro:'))
# variável acumulativa
fatorial = 1
#variável incremental
count = 1

while count <= num:
    # aqui fatorial vai se multiplicar a cada laço 1x1, 1x2,1x3...1xnum
    fatorial *= count
   # soma +1 em count para passar por cada elemento até chegar a num
    count += 1
print(fatorial)# imprime só resultado