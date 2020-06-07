'''
Faça um script que exibe uma lista de 10 elementos, contados de 1 até 10.
Depois, dobre cada valor dessa lista e exiba. Veja que agora são todos
pares.
'''

numeros = []
# usar range(1,11) para dobrar os valores ali contidos
for count in range(1,11):
    #concatenamos o valor a lista numeros
    numeros += [count]
#Para acessar todos os elementos, vamos usar uma range que vai de 0 até o tamanho da lista, que é len(numeros)
for count in range(len(numeros)):
    # dobrando cada valor lista 
    numeros[count] = numeros[count]*2
# imprimindo elementos dobrados 
for count in numeros:
    print(count)