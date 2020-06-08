# lista é uma sequência ordenada de elementos, cada qual associado a um número responsável por indicar a sua posição. Este número é denominado índice. O primeiro índice de uma lista é sempre 0, o segundo 1, e assim por diante. 


# Os elementos de uma lista não precisam ser do mesmo tipo
lst_mista = ['Ana', 9.5, [10, 20, 30]]

# é possível usar a função list() para criar uma lista a partir de uma string 
lst = list("Recife") # vai gerar a lista ['R','e','c','i','f','e']

# Operações sobre Listas
# Operações de Indexação, Fatiamento, Iteração, Busca e Modificação em Listas.

# Processamento básico de listas
lst_bichos = ['bem-te-vi', 'capivara', 'saracura', 'teiú']
# nossa conhecida função len() pode ser utilizada p/obtermos o tamanho (número de elementos) da lista
tam_lista = len(lst_bichos) 

#(1)-indexando os elementos
primeiro = lst_bichos[0] #retorna 'bem-te-vi'
ultimo = lst_bichos[3] #retorna 'teiú'
ultimo_tambem = lst_bichos[-1] #também retorna 'teiú'
print('lst_bichos: ', lst_bichos)
print('tipo de dado: ', type(lst_bichos))
print("total de elementos: ", tam_lista)
print("primeiro elemento: " + primeiro)
print("último elemento: " + ultimo)
print("último elemento de novo: " + ultimo_tambem)
print('---------------')

#(2)-iteração: percorrendo os elementos com um laço for-in
k=1;
for b in lst_bichos:
    print('elemento ', k, ' = ', b)
    k = k+1
print('---------------')

#(3)-fatiamento: obtendo sublistas (slices)-> ver sintaxe abaixo
print(lst_bichos[0:2]) #['bem-te-vi','capivara']
print(lst_bichos[2:4]) #['saracura','teiú']
print(lst_bichos[:2]) #['bem-te-vi','capivara']
print(lst_bichos[2:]) #['saracura','teiú']
print('---------------')

#(4)-operador in (busca): elemento pertence à lista?
# o operador in para testarmos se um determinado elemento pertence à lista (True ou False será retornado)
tem_capivara = 'capivara' in lst_bichos
tem_piton = 'píton' in lst_bichos
print("'capivara' está na lista? -> ", tem_capivara)
print("'píton' está na lista? -> ", tem_piton)
print('---------------')

#(5)-modificando o conteúdo 
# procedimento básico para modificar o conteúdo da lista
# podemos modificar o elemento, bastando indicar seu índice ou vários de uma vez, utilizando a mesma notação empregada na operação de fatiamento.
lst_bichos[2] = 'sabiá' #altera o elemento de índice 2
print("nova lista -> ", lst_bichos)
lst_bichos[:2] = ['bicudo','preá'] #altera os elementos 0 e 1
print("novíssima lista -> ", lst_bichos)


# Sintaxe da operação de fatiamento de listas
'''
• lst[i:j]: do elemento de índice i ao de índice j-1.
• lst[i:]: do elemento de índice i até o último da lista.
• lst[:j]: do primeiro elemento da lista (índice 0) ao elemento de índice j-1.
• lst[i:j:k]: do elemento de índice i, até, no máximo, o de índice j-1,utilizando o passo k.
• lst[-k:]: obtém os k últimos elementos da lista.
• lst[:-k]: em uma lista com n elementos, retornará os primeiros n-k elementos.
'''