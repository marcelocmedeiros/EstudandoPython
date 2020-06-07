'''
Pedimos um inteiro positivo, de quantos elementos o usuário deseja ver.
Em seguida, criamos a lista, com o valor de 1 dentro, que é quanto vale 0!

Agora, entramos no for. Que vai calcular o valor do termo de índice 1, termo
de índice 2, termo de índice 3...até o valor de termo n-1.

Para calcular cada novo termo, basta pegar o termo anterior e multiplicar
pelo índice atual, afinal:
n! = n * (n-1)!
'''

n = int(input("Gerar sequencia até o termo: "))
fat = [1]
for count in range(1,n):
    # ele vai multiplicar sempre pelo último termo da lista assim sempre gerando seu fatorial
    termo = fat[count-1]*count
    # add a lista
    fat += [termo]
print("Fatoriais: ",fat)