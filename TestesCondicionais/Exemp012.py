# Operador OR em Python
# # teste condição1 or condição2 or ...| O teste vai retornar TRUE somente se uma das condições forem TRUE! E só retorna False se todas forem False
'''
Para ter acesso a fila de prioridade, você deve ser idoso, gestante ou cadeirante. Escreva um programa que pergunta a situação do usuário (se éidoso, se é gestante, se é cadeirante ou nenhum destes) e diga se ele pode ter acesso a fila prioridade ou não.
'''

print('1. Idoso')
print('2. Gestante')
print('3. Cadeirante')
print('4. Nenhum destes')
resposta=int( input('Você é: ') )
if (resposta==1) or (resposta==2) or (resposta==3) :
    print('Você tem direito a fila prioritária')
else:
    print('Você não tem direito a nada. Vá pra fila e fique quieto')
    