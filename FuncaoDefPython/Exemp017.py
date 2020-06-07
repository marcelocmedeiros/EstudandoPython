# Recursividade

# Somatório
"""def somatorio(x):
    # quando argumento for 1 ela retorna 1 e finaliza
    if x==1:
        return 1
    # se não ela entra em um loop decrescente até chegar no valor 1 efetuando a operação
    else:
        return x + somatorio(x-1)


while True:
    x = int(input("Somatorio de 1 até: "))
    print("Soma: ",somatorio(x) )"""

# fatorial

def fatorial(x):
    # quando argumento for 1 ela retorna 1 e finaliza
    if x==1:
        return 1
    # se não ela entra em um loop decrescente até chegar no valor 1 efetuando a operação
    else:
        return x * fatorial(x-1)


while True:
    x = int(input("Fatorial de: "))
    print("Fatorial: ",fatorial(x) )