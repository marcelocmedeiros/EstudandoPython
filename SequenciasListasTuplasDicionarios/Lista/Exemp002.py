'''
O print do exemplo anterior está muito feio. Entre colchete, com aspas, vírgulas...faça um print bonitinho, onde cada linha é uma informação e dizendo que informação é aquela
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

print("Nome : ", eu[0])
print("Idade : ", eu[1], "anos")
print("Altura: ", eu[2],"m")
print("Peso : ", eu[3],"kg")
print("Casado: ", eu[4])