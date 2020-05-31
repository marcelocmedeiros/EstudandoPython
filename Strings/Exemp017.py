'''
Expressão Regular: O que é? Para que serve ?
As expressões regulares vão atuar: você vai definir um padrão e elas vão buscar no texto esse padrão.
As regular expressions (breviação Regex) são isso: padrão de um texto que vamos procurar.
'''

"""
Crie uma função que recebe um argumento do tipo string, e diz se ela representa um telefone do tipo xxxx-yyyy ou não
"""

def eTelefone(numero):
    if len(numero) != 9:
        print("Tamanho diferente de 9")
        return False
    for index in range(0,4):# sempre lembrar que o fim do range n-1==3 neste caso
        if numero[index].isdecimal() is not True:
            print("4 primeiros não são número")
            return False
    if numero[4] != '-':
        print("Nao tem hífen")
        return False
    for index in range(5,9):# sempre lembrar que o fim do range n-1==8 neste caso
        if numero[index].isdecimal() is not True:
            print("4 ultimos nao sao numero")
            return False

    return True

while True:
    numero = input("Numero no formato 'xxxx-yyyy': " )
    # chamei a função eTelefone
    if eTelefone(numero) is True:
        print("Válido")
    else:
        print("Inválido")