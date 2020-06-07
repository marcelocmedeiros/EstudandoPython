'''
Faça um script que exiba a uma lista que tem os números de 1 até 10, na
seguinte maneira:
Numero 1: 1
Numero 2: 2
Numero 3: 3
Numero 4: 4
Numero 5: 5
Numero 6: 6
Numero 7: 7
Numero 8: 8
Numero 9: 9
Numero 10: 10
'''

numeros = []

for count in range(1,11):
    numeros +=[count]
# Para acessar todos os elementos da lista 
for count in range(len(numeros)):
    print('Número %2d: %2d' %(count+1, numeros[count]))
print(numeros)

