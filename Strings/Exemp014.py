'''
    Buscar no início da string: startswith(substring)
Analogamente, é possível verificar se alguma coisa está (uma string) está no
começo, bem no início de outra string, através do método startswith (do
inglês 'começa com'):
    • texto.startswith( substring )
'''

str = "Estou procurando em um texto por palavras chave, quero saber se elas existem no início do texto (string). Para " \
      "isso posso usar o método startswith "
print(str.startswith("texto"))
print(str.startswith("Texto"))
print(str.startswith("texto", 23, 100))
# provando que a parti do indice 23 da string começa com texto
print(str[23:])
print(str.startswith("Texto", 23, 100))
print(str.startswith("texto", 90, 100))
print(str[90:])