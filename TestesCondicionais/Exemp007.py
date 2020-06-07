'''
2.Faça um script que peça um valor e mostre na tela se o valor é
positivo ou negativo.
'''
num = int(input('Informe um número real: '))
if num > 0:
    print('O número %d é Positivo!'%num)
else:
    if num < 0:
        print('O número %d é Negativo!'%num)
    else:
        print('Você digitou %d que neutro!'%num)