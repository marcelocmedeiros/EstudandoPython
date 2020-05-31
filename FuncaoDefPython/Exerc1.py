"""
Escreva um script que pergunta ao usuário se ele deseja converter uma
temperatura de grau Celsius para Farenheit ou vice-versa. Para cada opção,
crie uma função. Crie uma terceira, que é um menu para o usuário escolher a
opção desejada, onde esse menu chama a função de conversão correta.
"""
# 1º crio uma def converter Celsius para Farenheit
def C_para_F(C):
    F = (C*9/5) + 32
    return F
# 2º crio uma def converter Farenheit para Celsius
def F_para_C(F):
    C = (F-32)*5/9
    return C
# 2º crio def menu
def menu():
    op = 1

    while op:
        op = int(input('0. Para encerrar o programa\n'
                       '1. Celsius para Farenheit\n'
                       '2. Farenheit para Celsius\n'
                       'Qual é sua opção: '))
        if op == 0:
            print('Programa encerrado!')
        elif op==1:
            C=int( input('Graus Celsius: ') )
            print('Convertido: ', C_para_F(C),' graus Farenheit\n')
        elif op==2:
            F=int( input('Graus Farenheit: ') )
            print('Convertido: ', F_para_C(F),' graus Celsius\n')
        else:
            print('Opção inválida')

# chamo a def menu
menu()
