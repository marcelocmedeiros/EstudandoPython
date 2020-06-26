'''
2. Faça um script que pede um número inteiro positivo ao usuário.
Em seguida, cria uma lista com igual número de itens, onde o primeiro termo
é 1!, o segundo é 2!, o terceiro é o valor de 3!, etc, até o termo que ele
digitou. Ou seja, se digitou n, vai exibir até o termo de índice n-1, e lá na lista
vai ter o valor de (n-1)!.
'''

n = int(input("Gerar sequencia até o termo: "))
fat = [1]
for count in range(1,n):
    # ele vai multiplicar sempre pelo último termo da lista assim sempre gerando seu fatorial
    termo = fat[count-1]*count
    # add a lista
    fat += [termo]
print("Fatoriais: ",fat)
