# Os operadores de comparação (==, !=, <, <=, >, >=) podem ser utilizados com strings.

'''
• Duas strings são iguais apenas se armazenam a mesma palavra, escrita de maneira idêntica, inclusive no que diz respeito às letras maiúsculas e minúsculas.
• As linguagens de programação não “agem” da mesma forma que as pessoas ao realizar comparações entre strings! Para as linguagens de programação, letras maiúsculas vêm antes das letras minúsculas. Isto ocorre porque as comparações entre strings são baseadas nos códigos internos dos caracteres e as letras maiúsculas possuem códigos menores do que as minúsculas. Por esse motivo, muitas vezes precisamos usar o método lower() (ou upper()) antes de comparar duas strings.
• De maneira análoga, caracteres acentuados possuem códigos maiores do que letras minúsculas e números códigos menores do que qualquer letra.
Caso você deseje mais informações a este respeito, pesquise sobre “complete ascii table” e “unicode utf-8 table” na Internet.
'''

# comparação de strings 

p1 = 'pássaro'
p2 = 'PÁSSARO'
p3 = '123'
print(p1=='pássaro') #True
print(p1=='PáSSaRo') #False
print(p1==p2) #False
print(p1.lower()==p2.lower()) #True
print(p3 < p1) #True
p1 = 'áaa'
p2 = 'aaa'
p3 = 'AAA'
print(p1==p2) #False
print(p2 < p1) #True
print(p2 < p3) #False