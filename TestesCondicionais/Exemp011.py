# Operador AND em Python
# teste condição1 and condição2 | O teste vai retornar TRUE somente se as DUAS condições forem TRUE!
'''
Para votar, você deve ter entre 18 anos e menos de 65 anos.
Escreva um programa que pergunte sua idade e diga se você é obrigado a
votar ou não.
'''
resposta=int( input('Qual sua idade: ') )
if resposta>=18 and resposta <=65:
    print('Você é obrigado a votar!')
else:
    print('Você não é obrigado a votar')