'''
• math.pi : constante matemática 3.14159...;
• math.e : constante matemática 2.718281... (número de Euler);

Funções de Arredondamento
    • math.ceil(x) : arredondamento “pra cima”, ou seja, retorna o menor inteiro com valor igual ou superior a x;
    • math.floor(x) : arredondamento “pra baixo”, ou seja, retorna o maior inteiro com valor igual ou inferior a x.
    • math.trunc(x) : truncamento, o que significa limitar o número de dígitos de x.

Funções Logarítmicas / Exponenciais

    • math.exp(x) : retorna e elevado a x;
    • math.log2(x) : retorna o logaritmo de x na base 2;
    • math.log10(x) : retorna o logaritmo de x na base 10;
    • math.log(x,b) : retorna o logaritmo de x na base b (de acordo com a documentação do Python, deve ser utilizada apenas quando b é diferente de 2 e 10).
    • math.pow(x,y) : retorna x elevado a y;
    • math.sqrt(x) : retorna a raiz quadrada de x;

Funções Trignométricas (em todas elas, x é um ângulo que deve ser fornecido em radianos)
    • math.acos(x) : retorna o arco cosseno de x;
    • math.asin(x) : retorna o arco seno de x;
    • math.atan(x) : retorna o arco tangente de x;
    • math.cos(x) : retorna o cosseno de x;
    • math.sin(x) : retorna o seno de x;
    • math.tan(x) : retorna a tangente de x;
    • math.degrees(x) : converte o ângulo x de radianos para graus;
    • math.radians(g) : converte o ângulo g de graus para radianos.
'''

# Exemplifica o uso de constantes e funções do módulo 'math'.
# módulo ‘math’
import math
#constante PI
print('PI=',math.pi) #3.141592653589793

#funções de arredondamento
x1 = 5.9
print('\n')
print(x1)
print('ceil',math.ceil(x1))
print('floor',math.floor(x1))
print('trunc',math.trunc(x1))

#logaritmo
print('\n')
x2 = 1024
print('log de',x2,'na base 2: ', math.log2(x2))

#imprime tabela com seno, cosseno e tangente de 30, 45 e 60
#note que é preciso converter os ângulos para radianos
print('\n')
for angulo_graus in range(30,61,15):
    angulo_radianos = math.radians(angulo_graus) # converter os ângulos para radianos
    print('\n* * * Angulo=',angulo_graus, ' graus')
    print('SENO =',round(math.sin(angulo_radianos),2)) # round aredenda p dois digitos
    print('COSSENO =',round(math.cos(angulo_radianos),2))
    print('TANGENTE =',round(math.tan(angulo_radianos),2))
