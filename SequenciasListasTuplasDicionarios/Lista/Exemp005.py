# Mudar Item em uma Lista

'''
Coloque uma opção para mudar o valor de um item. Você deve pedir a posição do índice (começando de 0) e o valor para mudar. Se o usuário
escolher um valor superior ao existente, exibe uma mensagem de erro.
'''
bandas = []

while True:

    op =int(input("1. Adicionar banda\n"
    "2. Exibir bandas favoritas\n"
    "3. Tamanho da lista\n"
    "4. Mudar valor de item\n"
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
    if(op==4):
        print('=-'*15)
        index=int(input("Indice que vai alterar: "))
        print('=-'*15)
        if(index<len(bandas)):
            print('=-'*15)
            temp=input("Nome da banda: ")
            bandas[index] = temp
            print('=-'*15)
        else:
            print('=-'*15)
            print("Esse indice não existe")
            print('=-'*15)