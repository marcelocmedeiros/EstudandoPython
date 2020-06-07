'''
Faça com que o script anterior também calcule a soma de todos os
elementos na lista numeros e exiba seu resultado
'''
numeros = []
for count in range(10):
    #concatenamos o valor a lista numeros
    numeros += [count]
soma=0
for count in numeros:
    print(count)
    # somamos a variavel soma cada elemento da lista números
    soma += count
print("Soma: ", soma)