# Tamanho de uma lista: len() | sintax len(nome_lista)
'''
Crie um programa que pergunta se o usuário deseja adicionar uma nova banda na Lista ou exibir a lista. a exibir o tamanho atual da lista.
'''
bandas = []

while True:

    op =int(input("1. Adicionar banda\n"
    "2. Exibir bandas favoritas\n"
    "3. Tamanho da lista\n"
    "Qual sua escolha:"))
    if(op==1):
        print('=-'*15)
        banda=input("Digite nome da banda: ")
        bandas.append(banda)
        print('=-'*15)
    if(op==2):  
        print('=-'*15)
        print(bandas)
        print('=-'*15)
    if(op==3):
        print('=-'*15)
        print("Tamanho da lista: ", len(bandas))
        print('=-'*15)