'''
o método endswith() (do inglês 'termina com' ) para localizar uma
substring (passada como argumento para o método) dentro de uma string
maior, da seguinte maneira:
    • texto.endswith(substring)
'''

while True:
    texto = input("Digite o nome de um arquivo com sua extensão:" )
    if texto.endswith('.txt'):
        print("É um arquivo de texto")
    elif texto.endswith('.pdf'):
        print("É um arquvido do Acrobat Reader")
    elif texto.endswith('.png'):
        print("É uma imagem")
    else:
        print("Outro tipo de arquivo")