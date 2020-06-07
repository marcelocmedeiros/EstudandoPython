# Utilização de variáveis para armazenar informações de uma pessoa.

#P001: variáveis e tipos; funçoes type() e print()

#PARTE 1: declaração de variáveis
nome = 'Jane'
sobrenome = "Austen"
idade = 41
nota = 9.9
aprovado = True

#PARTE 2: imprimindo o conteúdo das variáveis print() e os tipos das mesmas type() 
print(nome, sobrenome, idade, nota, aprovado)
print(type(nome))
print(type(sobrenome))
print(type(idade))
print(type(nota))
print(type(aprovado))

#PARTE 3: mudando o valor e o tipo da variável “nota”
nota = 'A'
print('mudei o valor e o tipo de "nota" para: ', nota, ",", type(nota))

'''
fluxo de execução (ordem em que os comandos são executados pelo interpretador Python) é de 
cima para baixo, em sequência.
'''

# Comentários são textos ou frases definidos com o uso do símbolo #

'''
Os comentários são ignorados pelo interpretador Python na hora em que o programa é processado. 
Eles servem apenas para documentação, isto é, para serem lidos pelos humanos que estiverem 
analisando ou alterando o programa.
'''
