# Precedência de Operadores 
# Python tem uma regra, sobre qual operação fazer primeiro.
# Na ordem de importância, maior pra menor:
# resolva os parêntesis ()
# •Exponenciação: **
# •Multiplicação, divisão e resto da divisão: * / %
# •Adição e subtração: + -

'''
Faça um programa em Python que receba as notas de Português, Inglês e
Matemática de um aluno, e em seguida forneça a média aritmética dessas
notas.
'''

port = float(input('Informe a sua nota:'))
ingl = float(input('Informe a sua nota:'))
matem = float(input('Informe a sua nota:'))
# código da soma
soma = port + ingl + matem
# código da média
media = soma/3
# código da média direto 1° resolve os () depois faz a divisão /
mediaDireta = (port+ingl+matem)/3
print('Média passo a passo:', media)
print('=-'*20)
print('Média direta código enxuto é:', mediaDireta)


