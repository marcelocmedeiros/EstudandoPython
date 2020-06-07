'''
Um número é dito perfeito quando ele é igual a soma de seus fatores. Por
exemplo, os fatores de 6 são 1, 2 e 3 (ou seja, podemos dividir 6 por 1, por 2
e por 3) e 6=1+2+3, logo 6 é um número perfeito. Escreva uma função que
recebe um inteiro e dizer se é perfeito ou não. Em outra função, peça um
inteiro n e mostre todos os números perfeitos até n.
'''

def perfeito(n):
    # código da def
    # somatorio dos número divisores de "n"
    soma = 0
    # laço for percorrer todos os números menores q "n" q podem ser divisores dele
    for val in range(1, n):
        # vai dividir "N" por todos os número menores q ele
        if n % val == 0:
            # soma o valor q for divisor de "n"
            soma += val
    # se somatorio dos divisores de "n" == n
    if soma == n:
        # é perfeito
        return True
    else:
        return False
def exibe():
    n = int(input("Exibir perfeitos até o número: "))
    # laço for vai jogar de 1 até n na função perfeito()
    for val in range(1, n + 1):
        if (perfeito(val)):
            #  exibir os números que retornarem True
            print(val)
while True:
    exibe()