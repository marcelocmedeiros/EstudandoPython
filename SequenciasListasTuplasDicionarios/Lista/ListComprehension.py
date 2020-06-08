# List Comprehension é uma notação matemática que facilita a criação e manipulação de listas

# Sintaxe: lst = [x for x in sequência]

# alguns exemplos:
'''
Notação Matemática          List Comprehension
A = {x^3 | 0 ≤ x ≤ 10}       A = [x*x*x for x in range(11)]
B = {1/2, 1/4, …, 1/10}     B = [1/x for x in range(2,11,2)]
C = {0, 0                   C = [([0]*2) for linha in range(5)]
0, 0
0, 0
0, 0
0, 0}

D = {x | 0 < x < 20 e x é ímpar} D = [x for x in range(20) if x%2==1]
'''
A = [x*x*x for x in range(11)]
print(A)
print('---------------')
B = [1/x for x in range(2,11,2)]
print(B)
print('---------------')
print('---------------')
C = [([0]*2) for linha in range(5)]
print(C)
print('---------------')
D = [x for x in range(20) if x%2==1]
print(D)
