'''
Crie um programa que peça um número ao usuário e imprima todos os
números pares de 1 até o número fornecido
'''
valor = int(input('Informe um num maior que 1: '))
print('Números pares entre 1 e', valor)

n=1 # variável contadora

while n <= valor:
    if n % 2 == 0:
        print(n, end=' ') # end= ' ' para deixa os nº todos na mesma linha
    n += 1