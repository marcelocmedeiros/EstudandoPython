#Expressões

'''
Os operadores +, -, *, /, e ** são usados, respectivamente, para realizar:
        + adição;
        - subtração;
        * multiplicação;
        / divisão;
        ** exponenciação;
        // retorna o quociente de uma divisão inteira;
        % retorna o módulo (resto).
ordem básica  de resolução é PEMDAS
    Parênteses
    Exponenciação
    Multiplicação
    Divisão
    Adição
    Subtração.
'''
# Matemática básica

#Adição, subtração, multiplicação e divisão
x=5; y=2
print(x+y, x-y, x*y, x/y)
print(y**x)

#quociente e resto (ou módulo)
quociente = x // y
modulo = x % y
print("O quociente da divisão de", x, "por", y, "é: ", quociente)
print("O módulo da divisão de", x, "por", y, "é: ", modulo)

#expressão com parênteses
minha_expressao = (1 + 2) * 5**2 / ((5-3) + 1)
print("O valor da expressão 'minha_expressao' é: ", minha_expressao)

#a divisão de dois inteiros sempre gera um float
#(mesmo que a divisão seja exata)
a=10; b=5; c=a/b
print(a, b, c)
print(type(a), type(b), type(c))

# Observações Imprtantes... 
'''
É possível escrever mais de um comando em uma única linha, bastando separá-los por ponto e vírgula. Por exemplo: a=10; b=5; c=a/b . Entretanto, de acordo com as “boas práticas de programação” (PEP-8), você deve evitar produzir uma linha que possua mais de 72 caracteres.
'''