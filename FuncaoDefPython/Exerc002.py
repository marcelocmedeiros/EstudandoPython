# def com 1 parametro
def cubo(x):
    # código da def
    cub = x**3
    print('O cubo de', x, 'é:', cub)

# progr principal pede um número
num = int(input("Informe um número inteiro: "))
# chamando a def
cubo(num)