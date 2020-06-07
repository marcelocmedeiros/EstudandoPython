# Matriz: Lista dentro de Lista

#Como inicializar uma matriz

#inicializar uma lista de 4 elementos
[0 for i in range(4)]
# inicializar uma lista de 4 elementos
matriz = [ [0 for i in range(4)] for j in range(4)]
# repetirmos o código anterior dentro de outro for
print(matriz) # imprime as 4 matrizes sem ainda está no formado de matriz

# exibir como uma matriz

matriz = [ [0 for i in range(4)] for j in range(4)]
# contador q add valores a matriz
count=0
# laço for p preenchimento de valores da matriz
for linha in range(4):
    for coluna in range(4):
        matriz[linha][coluna] = count
        count += 1
    # aqui vai imprimir em linha sem formatação    
    print(matriz) 

# código da formatação da matriz (como ela será exibida)
for linha in range(4):
    for coluna in range(4):
        # %4d quer dizer com 4 espaços | end='' paralaço for deixa todos na mesma lista 
        print("%4d" % matriz[linha][coluna], end='')
    # este print vazio dentro do 1° for que da forma de matriz p impresão pq ele quebra a linha no final
    print()

