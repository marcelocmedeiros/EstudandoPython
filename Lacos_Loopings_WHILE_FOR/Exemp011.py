'''
Crie um script em Python que imprima os números pares de 1 até 100
'''

# range com 3 argumentos incio, fim e pulo (inicio=2, fim=101, pula=2)

for val in range(2, 101, 2):
    # 1° variá vai impimir o 2
    # depois ela vai pular de 2 em 2 e imprimir o número
    # fim n - 1, então vai até 101 - 1 == 100
    print(val, end=' ')