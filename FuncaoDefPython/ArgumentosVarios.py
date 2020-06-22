# não sabemos com antecedência quantos argumentos a função vai receber , podemos criar um parâmetro onde simplesmente adicionamos uma asteriscos na frente do parâmetro e ele pode receber quantos argumentos forem necessários ou nenhum argumento. 


# Programa pizza

def pizza(tamanho, *ingredientes):
    print('\nPizza', tamanho)
    print('Com:', end=' ')
    for i in ingredientes:
        print(i, end=', ')
    print()

tamanho = input('Entre com o tamanho ("media", "grande", "brotinho"): ')
ingredientes = input('Entre com os ingredientes: ')

li = ingredientes.split()

pizza(tamanho, li)