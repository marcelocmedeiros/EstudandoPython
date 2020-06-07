# Adicionar Item em uma lista: métodlo append()| sintax: "nome_lista.append()"
'''
Crie um programa que pergunta se o usuário deseja adicionar uma nova banda na Lista ou exibir a lista.
'''
bandas = []

while True:

    op =int(input("1. Adicionar banda\n"
    "2. Exibir bandas favoritas\nQual sua escolha:"))
    if(op==1):
        banda=input("Digite nome da banda: ")
        bandas.append(banda)
    if(op==2):  
        print(bandas)