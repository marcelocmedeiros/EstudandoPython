"""
Faça um programa que pergunta o gênero da pessoa. Se ela for mulher,
digite 1. Se for homem, digite 2. Outro, 3.
"""

sexo = int( input('Digite 1 se for mulher, 2 homem ou 3 outro: ') )
if sexo == 1:
    print('Você é mulher')
if sexo == 2:
    print('Você é homem')
if sexo == 3:
    print('Outro gênero')
    