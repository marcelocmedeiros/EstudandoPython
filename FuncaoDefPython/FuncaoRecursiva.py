# Função recursiva
# Calculo do fatorial

def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial(numero-1)


x = int(input("Digite um número: "))

res = fatorial(x)

print(f'O fatorial de {x} é {res}')
print('O fatorial de {} é {}'.format(x, res))
print('O fatorial de %d é %d'%(x, res))

# Sequência de Fibonacci recursiva
'''
"""
0,1,12,3,5,8,13,21,34
Fibonacci(num) = num , se num <=1, e 
Fibonacci(num) = Fibonacci(num-1) + Fibonacci(num - 2), para num > 1 
"""
def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num - 2)

x = int(input("Digite um número: "))

res = fibonacci(x - 1)

print(f'A sequência de fibonacci de {x} é {res}')
print('A sequência de fibonacci de {} é {}'.format(x, res))
print('A sequência de fibonacci de  %d é %d'%(x, res))
'''