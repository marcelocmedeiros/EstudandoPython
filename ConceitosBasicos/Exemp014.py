# Porcentagem e Juros Compostos

'''
Um cliente pediu que o sistema do banco tivesse a seguinte função:
Dizer o valor inicial que ele deve investir, para ao final de 'm' meses ele tenha
um valor 'vf', supondo que este dinheiro esteja rendendo uma rentabilidade 'i'
mensal, em porcentagem esse 'i'.
Faça um programa que pede o valor final, o tanto de meses que vai ficar
aplicado, a rentabilidade e o script mostre o valor inicial que ele deve investir
para atingir tal objetivo.
'''
# fórmula vf = vi * (1+i)**m
# Vf - Valor final na poupança, ao término do tempo
# Vi - Valor inicial que o cliente vai colocar na poupança
# i - Rentabilidade mensal (em porcentagem)
# m - Tanto de meses que o dinheiro do cliente vai ficar rendendo

# Valor inicial aplicado
vi = float( input('Valor inicial: ') )
# Rentabilidade mensagem, em %
i = float ( input('Rentabilidade mensal: ') )
# Transformando a porcentagem em valor numérico
i = i / 100
# Tempo de investimento
m = int( input('Meses que vai deixar rendendo: ') )
vf = vi * (1+i)**m
print('Valor apos ',m,' meses: R$ ',vf)
