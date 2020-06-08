'''
Funções Numéricas
    • abs(x) : retorna o valor absoluto de x;
    • pow(x,y) : retorna x elevado a y.
    • round(x,d) : retorna x arredondado para d casas decimais (neste caso, x deve ser um float).

Funções de String
    • len(s) : retorna o comprimento (número de caracteres) de s;
    • max(s) : retorna o maior caractere de s, considerando a ordem lexicográfica;
    • min(s) : retorna o menor caractere de s, considerando a ordem lexicográfica.

Funções de Conversão de Tipo
    • float(s) : converte a string s para um float. A variável s deve conter um número válido, inteiro ou float, caso contrário a função retornará um erro;
    • int(s) : converte a string s para um inteiro. A variável s deve conter um número inteiro válido, caso contrário a função retornará um erro;
    • str(n) : converte o número n para uma string. Seu uso é necessário quando você quer concatenar uma string com um número.
'''

# Exemplifica o uso das funções pré-definidas.
# funções pré-definidas
print("\n-------------------------")
print("* * funções numéricas * * " )
print("-------------------------\n")

#funções numéricas
n1=100
n2=3.141592653
n3=9.99
print(abs(1000), abs(-500), abs(2 * -2.5), abs(0)) #1000 500 5.0 0
print(pow(n1,2)) #10000
print(round(n2,2)) #3.14
print(round(n2), round(n3)) #3 10

print("\n----------------------------")
print("* * funções de conversão * * " )
print("----------------------------\n")
#funções de conversão
s1='5'
s2='9.99'

print(int(s1)) #converteu '5' -> 5
print(float(s2)) #converteu '9.99' -> 9.99
print('O valor de PI com 10 digitos é: ' + str(n2))
print('O valor de PI com 2 digitos é: ' + str(round(n2,2)))
print("\n-------------------------")
print("* * funções de string * * " )
print("-------------------------\n")
#funções de string
s1='python'
s2='inconstitucional'
print(len(s1)) #6
print(len(s2))  #16
print(max(s1)) #'y'
print(min(s1)) #'h'



