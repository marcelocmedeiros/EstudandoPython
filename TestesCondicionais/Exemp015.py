'''
Escreva um script que peça um número ao usuário.
Em seguida, ele deve descobrir se o número é inteiro ou decimal.Se for decimal, deve dizer o número arredondado pra cima e arredondado pra baixo.
'''

num = float(input('Numero original: '))
if num == round(num):
    print("Inteiro")
else:
    print("Decimal")
    print("Arredondado pra baixo: ", round(num-0.5) )# arredonda p baixo
    print("Arredondado pra cima : ", round(num+0.5) )# arredonda p cima
    