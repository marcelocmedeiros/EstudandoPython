# def com 1 parametro
def quadrado(x):
    # código da def
    quad = x*2
    print('O quadrado de', x, 'é:', quad)

# progr principal pede um número
num = int(input("Informe um número inteiro: "))
# chamando a def
quadrado(num)