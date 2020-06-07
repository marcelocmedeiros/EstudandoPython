'''
Faça um script que pede ao usuário um número inteiro positivo.
Em seguida, deve criar uma lista onde o primeiro termo é 0, o segundo é 1 e os outros são a sequência de Fibonacci. O número de termos é o que o usuário forneceu como número.
'''

n = int(input("Gerar sequencia até o termo: "))

fibo = [0,1]

for count in range(2,n):
    # estou somando sempre os dois últimos termos da lista -1 e -2
    termo = fibo[count-1] + fibo[count-2]
    fibo += [termo]
print("Sequência: ",fibo)