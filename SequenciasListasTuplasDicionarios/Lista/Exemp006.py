# Deletar Item de uma Lista: del item | sintax: del bandas[indice_da_lista]
'''
add ao programa anterio opção de deletar 
'''


bandas = []

while True:

    op =int(input("1. Adicionar banda\n"
    "2. Exibir bandas favoritas\n"
    "3. Tamanho da lista\n"
    "4. Mudar valor de item\n"
    "5. Deletar um intem da lista\n"
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
    if(op==5):
        print('=-'*15)
        index=int(input("Indice quer deletar: "))
        print('=-'*15)
        if(index<len(bandas)):
            print('=-'*15)
            print('Você deletou',bandas[index],'da sua lista')
            del(bandas[index])
            print('=-'*15)
        else:
            print('=-'*15)
            print("Esse indice não existe")
            print('=-'*15)