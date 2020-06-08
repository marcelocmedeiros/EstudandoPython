# Operações Básicas sobre Listas Bidimensionais.
# Processamento básico de listas bidimensionais
m = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12]
]
#(1)-indexando os elementos
print(m[0]) #retorna a primeira linha: [1, 2, 3, 4]
print(m[0][0]) #retorna 1 (elem da linha 0, col 0)
print(m[2][1]) #retorna 10 (elem da linha 2, col 1)
print(m[-1]) #retorna a última linha: [9, 10, 11, 12]
print(m[-2][3]) #retorna 8 (elem da penúltima linha, col 3)
print('---------------')

#(2)-iteração: percorrendo os elementos com laços for-in aninhados
linhas = len(m) #com len() obtemos o total de linhas
for y in range(linhas):
    cols = len(m[y]) #número de colunas da linha corrente
    for x in range(cols):
        print(m[y][x], end = " ")
    print();
print('---------------')

#(3)-modificando o conteúdo
m[0][0] = 99 #modifica o elemento da linha 0, col 0 p/ 99
m[2] = [4, 3, 2, 1] #modifica a linha 2 p/ [4, 3, 2, 1]
print("nova matriz: ")
print(m)
print('---------------')
#(4)-criando uma matriz dinamicamente
linhas=5
cols =2
m2 = []
for linha in range(linhas):
    m2 += [[0]*cols]
print("matriz criada dinamicamente: ")
print(m2)
print('---------------')