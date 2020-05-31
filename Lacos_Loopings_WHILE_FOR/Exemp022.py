'''
Escreva um programa em Python que vai somar todos os números de 1 até 1000,
menos os que são múltiplos de 3
'''
# armazena toda soma q não foi multiplo de 3
total = 0

for count in range(1000):
    # condição para pular o laço p próxima instrução
    if count % 3 == 0:
        continue
    # soma instrução q não foi pulada a total
    total += count

print(total)