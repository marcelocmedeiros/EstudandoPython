'''
Seu professor de Matemática, cansado de ficar fazendo multiplicações para
achar o fatorial, te encomendou um script em Python. Porém, ele quer fazer vários
e vários cálculos. Nos exemplos anteriores a gente pede o número uma vez, mostra o fatorial e
fecha o script. Ele não, ele quer um looping infinito, que só acabe quando ele fornecer o
número 0 como entrada.
'''
n = int(input("Digite um número inteiro positivo: "))
while n > 0:
    fatorial = 1
    while n > 1:
        fatorial *=n
        n = n-1
    print(fatorial)
    n = int(input("Digite um número inteiro positivo: "))


