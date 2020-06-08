'''
• s.lower(): retorna uma cópia de “s” convertida para minúsculo; Importante: esse método, assim como todos os outros, não altera a string original “s”, já que toda string é imutável!
• s.upper(): retorna uma cópia de “s” convertida para maiúsculo;
• s.find(sub, inicio, fim): verifica se "sub" ocorre na string “s” ou dentro de
algum trecho específico caso “início” e “fim” tenham sido definidos. Caso positivo, retorna o índice da primeira ocorrência. Senão retorna -1;
• s.rfind(sub, inicio, fim): igual ao método find(), porém faz a verificação de
trás para frente;
• s.endswith(sufixo, inicio, fim): verifica se “s” ou um trecho definido de “s”
(caso os parâmetros opcionais “início” e “fim” tenham sido especificados) termina com a substring especificada em "sufixo". Retorna True ou False;
• s.replace(sub_ant, sub_nova, max): retorna uma cópia da string “s” com as
ocorrências da substring "sub_ant" substituídas por "sub_nova". O parâmetro "max" pode ser utilizado para determinar o número máximo de trocas que serão realizadas.
• s.count(sub, inicio, fim): conta quantas vezes a substring "sub" aparece no
trecho de “s” demarcado por "inicio" e "fim" (se esses parâmetros forem omitidos procura na string toda).
• s.strip(): retorna uma cópia de "s" sem os espaços em branco à esquerda e à direita;
• s.lstrip(): retorna uma cópia de "s" sem os espaços em branco à esquerda;
• s.rstrip(): retorna uma cópia de "s" sem os espaços em branco à esquerda e à
direita;
• s.split(d,max): divide uma string em uma lista de strings, de acordo com o
delimitador "d" (se este não tiver sido fornecido, usa espaço em branco). O parâmetro "max" pode ser utilizado para determinar o número máximo de elementos da lista.
• s.translate(tabela, deletechars): este método é utilizado para traduzir
strings de acordo com uma tabela de tradução (parâmetro “tabela”) definida pelo método maketrans() (os dois métodos trabalham em conjunto). A sua utilização é um pouco complicada e nesse livro o utilizaremos apenas em sua forma básica, onde o parâmetro “deletechars” é utilizado para remover caracteres de uma string.
'''

# Métodos disponíveis para strings. Uma observação sobre o programa abaixo: não existe um método para retornar o comprimento de uma string! Para obter esse valor, você precisa utilizar a velha e boa função pré-definida len().

# Métodos de strings

p1 = 'Lagarto Teiú'

p1_maiusc = p1.upper()
p1_minusc = p1.lower()

num_letras_p1 = len(p1)
num_letras_a = p1.count('a')
testa_endswith = p1.endswith('rto',4,7)
testa_find = p1.find('a')
testa_rfind = p1.rfind('a')

p1_troca = p1.replace('a','o')
p1_split = p1.split()

p2 = ' Capivara ';
teste_strip = p2.strip();

p3 = 'ei, olha isso... uma capivara!'
sem_pontuacao = p3.translate(p3.maketrans('','',",.!")) #remove: , . !

print("p1.upper()= " + p1_maiusc)
print("p1.lower()= " + p1_minusc)
print("len(p1)= " + str(num_letras_p1))
print("p1.count('a')= " + str(num_letras_a))
print("p1.endswith('rto',4,7)= ",testa_endswith)
print("p1.find('a')= ",testa_find)
print("p1.rfind('a')= ",testa_rfind)
print("p1.replace('a','o')= " + p1_troca)
print("p1.split()= ", p1_split)
print("p2.strip()= *" + teste_strip + "*")
print("frase com pontuacao= " + p3)
print("frase sem pontuacao= " + sem_pontuacao)