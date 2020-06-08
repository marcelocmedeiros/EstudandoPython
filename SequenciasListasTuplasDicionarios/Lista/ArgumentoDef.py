# quando uma variável que armazena um valor primitivo (int, float, string ou boolean) é passada como argumento de uma função, ela é sempre um parâmetro de valor. Isto significa que qualquer alteração no conteúdo da variável que tenha sido realizada dentro do bloco de código da função, não será refletida para o programa principal

# No caso de um objeto complexo (como uma lista, dicionário, conjunto, etc.) é passado como argumento de uma função, ele será sempre um parâmetro de referência. Isto significa que alterações realizadas no formato ou conteúdo do objeto serão permanentes, ou seja, serão refletidas para o programa principal. 

# Passando um objeto de tipo complexo (lista) como argumento de função.
# argumentos de função:
# variável de tipo primitivo (int) x de tipo complexo (lista)
def f_dummy(z):
    if type(z) == list:
        z[0] = 999
    else:
        z = 999

        
x = 0
lst = [1,2,3,4,5]
print('x antes de chamar a função f_dummy:',x)
f_dummy(x)
print('x depois de chamar a função f_dummy:',x)
print('----------------------------------------')
print('lst antes de chamar a função f_dummy:',lst)
f_dummy(lst)
print('lst depois de chamar a função f_dummy:',lst)