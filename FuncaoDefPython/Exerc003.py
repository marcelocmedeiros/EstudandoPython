# def com 4 parametros
def media(x, y, z, w):
    # código da def
    calc = (x+y+z+w)/4
    print('A média das notas é:', calc)

# progr principal pede um número
num1 = int(input("Informe 1ª nota: "))
num2 = int(input("Informe 2ª nota: "))
num3 = int(input("Informe 3ª nota: "))
num4 = int(input("Informe 4ª nota: "))
# chamando a def
media(num1, num2, num3, num4)