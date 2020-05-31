'''
Achar qualquer substring em qualquer lugar de uma string:
    find()
    vai retornar o menor índice da primeira aparição dessa substring.
    Se não encontrar, retorna -1
'''

str = "Estou procurando em um texto por palavras chave, quero saber se elas existem e onde no texto (string) começam. Para isso posso usar o método find"
print(str.find("texto"))
print(str.find("Texto"))
print(str.find("texto", 24, 100))