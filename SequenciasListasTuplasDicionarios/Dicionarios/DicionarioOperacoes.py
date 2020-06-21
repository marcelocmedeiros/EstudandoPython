# Dicionário é uma estrutura de dados em que os elementos são pares chave:valor. A chave (key) identifica um item e o valor (value) armazena o conteúdo do mesmo

# Diferenças entre dicionários X listas: 1- em uma lista, os índices que determinam a posição dos elementos precisam ser inteiros. 2- em um dicionário os índices podem ser não apenas inteiros, mas também de qualquer tipo básico imutável, como strings e tuplas. 3- não existe o conceito de ordem, ou seja, ele é uma coleção não ordenada de pares chave:valor

# As chaves de um dicionário só podem ser de um tipo imutável como inteiros, floats e strings. Tuplas também podem ser aceitas desde que não contenham direta ou indiretamente um tipo mutável como listas.

# Dicionários não possuem uma noção de índice e não podem ser fatiados.

# Dicionários são mutáveis de forma que a qualquer momento você pode inserir ou remover itens.

# Ex: dic_alunos = {'M01':'Jane','M13':'George','M15':'Thomas','M04':'Aldous'}

# Observe que: (i) chaves "{ }" foram utilizadas para criar o dicionário; (ii) dentro das chaves, o símbolo de dois-pontos ":" é utilizado para separar a key de seu valor; e (iii) os diferentes elementos são separados por vírgulas.

# Operações Básicas

# Operações de Inserção/Remoção de Itens, Busca e Modificação

# Dicionário: criação e manipulação básica

dic_alunos = {'M01':'Hane','M13':'George','M15':'Thomas'}
print('dic_alunos (original): ', dic_alunos)

#insere novo aluno (novo par chave:valor)
dic_alunos['M04'] = 'Aldous'

#altera o valor associado à chave 'M01' para Jane
dic_alunos['M01'] = 'Jane'

#remove o elemento de chave 'M15'
del dic_alunos['M15']

#checando se uma chave existe
tem_M13 = 'M13' in dic_alunos #retorna True
tem_M99 = 'M99' in dic_alunos #retorna False

print('dic_alunos (após alterações): ', dic_alunos)
print('tipo de dado: ', type(dic_alunos))
print('existe a mat. M13?: ', tem_M13)
print('existe a mat. M99?: ', tem_M99)
