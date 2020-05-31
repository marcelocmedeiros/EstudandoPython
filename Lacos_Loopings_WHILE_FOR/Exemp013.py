'''
Crie um programa que pergunte ao usuário o termo inicial e a razão de uma PA.
Em seguida, pergunte a ele quantos elementos da PA ele deseja que seja
impresso, e imprima todos os elementos dessa progressão Aritmética, do
primeiro termo até o termo 'n' escolhido pelo usuário.
'''

termoInc = int(input('Qual o termo inicial:'))
razao = int(input('Qual a razão da PA.:'))
elementos = int(input('Quantos elementos da PA você deseja:'))
#código a = a1 + (n-1)*r
termoFim = termoInc + (elementos - 1)*razao

# usando loaço For para exibir os elementos
for var in range(termoInc, termoFim+1, razao):
    # range imprime incio até o fim - 1 | então soma+1 ao fim para fim ser impresso
    print(var, end='->')