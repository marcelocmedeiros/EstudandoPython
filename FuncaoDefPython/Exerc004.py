# def com 3 parametros
def maior(x, y, z):
    # código da def
    if x > y and x > z:
        mai = x
    elif y > x and y > z:
        mai = y
    else:
        mai = z
    print('O maior número entre os Três é:', mai)

# progr principal pede um número
num1 = int(input("Informe 1ª número: "))
num2 = int(input("Informe 2ª número: "))
num3 = int(input("Informe 3ª número: "))

# chamando a def
maior(num1, num2, num3)