# Estruturas Aninhadas - IF ELSE dentro de IF ELSE
# Corrigindo Bugs do programa anterior

print('1. Corinthians')
print('2. Flamengo')
resposta = int (input('Qual melhor time: ') )
if resposta == 1:
    print('Você deve ser corinthiano')
else:
    if resposta == 2:
        print('Você deve torcer Flamengo')
    else:
        print('Certamente você não torce Corinthians nem Flamengo')

