'''
Crie um programa que peça um número inteiro positivo ao usuário.
Em seguida, o script deve mostrar os números de 0 até o valor que o
usuário escolheu. Use WHILE.
'''

num = int(input('Digite um número inteiro positivo:'))

count = 0
while count <= num:
    print(count, end=' ')
    # incrementando a variável count +1
    count +=1
