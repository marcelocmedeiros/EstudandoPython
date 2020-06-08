# A função print() serve para imprimir um ou mais objetos (mensagens, números, listas, etc.)

# Parâmetros e operadores que podem ser utilizados para enriquecer as funcionalidades de print()

# Print() revisitado
a=1; b=2; c=3

#imprime os valores de "a", "b" e "c" separados por espaço
print(a,b,c) #1 2 3

#parâmetro "sep": troca espaço pelo separador especificado
print(a,b,c,sep=';') #1;2;3

#parâmetro "end": por padrão, a função termina uma linha com \n (quebra de linha)
#Mas você pode terminar com qualquer caractere usando o parâmetro "sep"
print("Meu Primeiro",end=' ')
print("Livro",end=' ')
print("de Python")

#a função format() facilita a impressão e formatação de dados de variáveis
#consulte: https://pyformat.info/
nome='PI'
v=3.14159;
print("{} com duas casas decimais={:.2f}".format(nome,v)) #PI ... 3.14

#o operador especial % permite a formatação no estilo “Linguagem C”
#consulte: https://www.learnpython.org/en/String_Formatting.
print("PI convertido para string=%s" % v) #’3.14159’

# O mais novo tipo de print formatado é 
nome = "Marcelo"
idade = 42

print(f'Meu nome é {nome} e tenho {idade} anos.')

#o sinal de escape (\) também permite a impressão de aspas
print("Imprimindo aspas \"") #imprimindo aspas "
print('Imprimindo aspas \'')#imprimindo aspas '

print('Imprimindo com "aspas"') # basta trocar as aspas se abriu com simples coleque dupla dentro 
print("Imprimindo com 'aspas'") # basta trocar as aspas se abriu com duplas coleque simples dentro 

#adicionando quebras de linha com \n
print("linha1\nlinha2\nlinha3")

#separando valores por tabulação com \t
print("coluna1 \tcoluna2 \tcoluna3")