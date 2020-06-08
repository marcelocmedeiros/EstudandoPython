# Função com parâmetro opcional. 
# Neste programa, a função “soma_numeros()” possui três parâmetros (“x”, “y” e “z”), mas o terceiro recebe o valor None como default. Com isto, você poderá chamar a função passando dois ou três números como parâmetro. No primeiro caso, ela retornará x + y e no segundo x + y + z.

# função com parâmetro opcional

# criando a def | z=None parametro opcional
def soma_numeros(x,y,z=None): # pode ser entendido como “ausência de qualquer coisa
    if (z==None):
        return x+y
    else:
        return x+y+z

# chando a def com 2 ou 3 argumentos
print(soma_numeros(1, 2))
print(soma_numeros(1, 2, 3))

# Além de None pode atribuir qualquer outro valor default para os parâmetros opcionais.
# Função com parâmetro que possui valor default. 
# Definição da função “f_calcula()”, cujo terceiro parâmetro (“operacao”) possui o valor “+” como default. Se o usuário chamar a função sem passar o terceiro parâmetro, o valor “+” será automaticamente adotado. 
print("\n---------------------")
print("* * Exemplo 2 * * " )
print("----------------------\n")
# função com parâmetro que possui valor default
def f_calcula(x,y,operacao='+'):
    if (operacao=='+'):
        return x+y
    elif (operacao=='-'):
        return x-y
    elif (operacao=='*'):
        return x*y
    elif (operacao=='/'):
        return x/y
    else:
        return 'operação inválida!'


print(f_calcula(1,2))       #retorna -> 1+2 = 3
print(f_calcula(1,2, '+'))  #retorna -> 1+2 = 3
print(f_calcula(1,2, '-'))  #retorna -> 1-2 = -1
print(f_calcula(1,2, '*'))  #retorna -> 1*2 = 2
print(f_calcula(1,2, '/'))  #retorna -> 1/2 = 0.5
print(f_calcula(1,2, '.'))  #retorna -> 'operação inválida'
