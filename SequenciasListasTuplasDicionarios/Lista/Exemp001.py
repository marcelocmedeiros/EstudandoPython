'''
Crie um programa em Python que peça seu nome, sua idade, sua altura, seu peso e True se for casado ou False para solteiro.
Em seguida, ele deve armazenar todas essas informações numa lista chamada eu. Por fim, imprima essa lista na tela.
'''

nome = str(input('Qual seu nome: '))
idade = int(input('Qual sua idade: '))
altura = float(input('Qual sua altura: '))
peso = float(input('Qual seu peso: '))

op= int(input("Estado civil:\n1.Casado\n2.Solteiro\n"))
if op==1:
    op = True
else:
    op = False
# armazenei tudo na lista eu=[]
eu = [nome, idade, altura, peso, op]
print(eu)