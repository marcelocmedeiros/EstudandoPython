# Operador NOT em Python

'''
Se era uma condição TRUE, ela vira FALSE.
Se algo era FALSE, ela vira TRUE.
Basta colocar not antes.
'''
# Se ele não digitar 'rush', chama o usuário de herege.

banda = input('Qual melhor time do Brasil? ')
if not banda=='Corinthians':
    print('Herege!')
else:
    print('Correto, é o Corinthians!')