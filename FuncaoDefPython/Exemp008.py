# função com 2 parametros
def calculadora(x,y):
    # código da def
    print("Soma =",x+y)
    print("Subtração =",x-y)
    print("Divisão =",x/y)
    print("Multiplicação =",x*y)

#prog princial q pede para usuario informar 2 números
primeiro = float(input("Primeiro número: "))
segundo = float(input("Segundo número: "))
#chamo a def calculadora com 2 argumentos
calculadora(primeiro,segundo)