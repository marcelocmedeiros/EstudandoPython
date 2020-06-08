# Repetição e concatenação de listas
lst1 = ['UFF','Niterói','RJ']
lst2 = ['Brasil']
#repetição: operador *
print(lst1*3) #['UFF','Niterói','RJ','UFF','Niterói','RJ','UFF','Niterói','RJ']
#concatenação: operador +
print(lst1 + lst2) #['UFF','Niterói','RJ','Brasil']

# Métodos

# uma lista Python é também um objeto

# para chamar um método, devemos adicionar um ponto (“.”) e o nome do método ao final do nome de uma lista

# considere que “lst” é uma lista e “e” um elemento
'''
                Métodos disponíveis para listas

• lst.append(e): adiciona o elemento “e” à “lst”. Análogo ao comando lst+=e;
• lst.clear(): remove todos os elementos da lista;
• lst.count(e): conta o número de ocorrências de “e” em “lst”;
• lst.extend(lst2): insere a lista “lst2” no final de “lst”;
• lst.index(e): retorna o menor índice de “e” em “lst”;
• lst.insert(pos, e): insere o objeto “e” na posição “pos” de “lst”;
• lst.remove(e): remove o elemento “e” de “lst”;
• lst.reverse(): inverte a lista;
• lst.sort(): ordena os elementos de “lst”.
'''

# Exemplifica o uso dos métodos da ED lista.
# Métodos disponíveis para listas

numeros = [0, 10, 15, 10, 20]
print("lista original: ", numeros)

quantos_10 = numeros.count(10) #retorna 2
print("num. de ocorrências do valor 10: ", quantos_10)

i_10 = numeros.index(10) #retorna 1
print("índice da primeira ocorrência de 10: ", i_10)

numeros.append(5) #adiciona o valor 5 no final da lista
print("lista modificada1: ", numeros)

numeros.insert(1,1000) #insere 1000 como segundo elemento
print("lista modificada4: ", numeros)

numeros.remove(10) #remove o primeiro elemento 10
print("lista modificada3: ", numeros)

numeros.extend([50, 60]) #adiciona a lista [50, 60] no final
print("lista modificada5: ", numeros)

numeros.sort() #ordena
print("lista ordenada: ", numeros)

numeros.reverse() #inverte
print("lista reversa: ", numeros)

numeros.clear() #esvazia a lista
print("lista vazia: ", numeros)
