
'''
Você deve criar um programa que pede 'Digite um número de 1 até 10', e de
acordo com o número fornecido pelo usuário, indicar qual o time está
naquela posição do ranking.
1	FLAMENGO	
2	SANTOS	
3	PALMEIRAS	
4	GRÊMIO	
5	ATHLETICO	
6	SÃO PAULO	
7	INTERNACIONAL	
8	CORINTHIANS	
9	FORTALEZA	
10	GOIÁS
'''

resposta=int(input('Que colocação no ranking deseja saber: '))
if resposta == 1:
    print('FLAMENGO')
elif resposta == 2:
    print('SANTOS')
elif resposta == 3:
    print('PALMEIRAS')
elif resposta == 4:
    print('GRÊMIO')
elif resposta == 5:
    print('ATHLETICO')
elif resposta == 6:
    print('SÃO PAULO')
elif resposta == 7:
    print('INTERNACIONAL')
elif resposta == 8:
    print('CORINTHIANS')
elif resposta == 9:
    print('FORTALEZA')
elif resposta == 10:
    print('GOIÁS')
else:
    print('Só temos até o décimo!')