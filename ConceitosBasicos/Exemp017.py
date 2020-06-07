# Formatando números na função print

# %f == float
# %d ou %i == inteiro
# %str == string

# Prêmio da Mega-Sena
total = float( input('Premio total da Mega: ') )
# Número de ganhadores
num = int( input('Numero de ganhadores: ') )
print('Cada um vai ficar com R$ ', (total/num) )
print('=-'*20)

# Formatando Números em Python
print('Cada um vai ficar com R$ %.0f' % (total/num) )# imprime sem casa decimal
print('=-'*20)
print('Cada um vai ficar com R$ %f' % (total/num) )# imprime sem formatação
print('=-'*20)
print('Cada um vai ficar com R$ %.1f' % (total/num) )# imprime com 1 casa decimal
print('=-'*20)
print('Cada um vai ficar com R$ %.2f' % (total/num) )# imprime com 2 casa decimal
print('=-'*20)
print('Cada um vai ficar com R$ %.3f' % (total/num) )# imprime com 3 casa decimal
print('=-'*20)
print('O premio total foi R$%.2f para %d ganhadores, onde cada um ficou \
com R$%.2f' %(total,num,total/num)) # %.2f float com 2 casa decimais | % d inteiro | \ quebra de linha dentro do código

