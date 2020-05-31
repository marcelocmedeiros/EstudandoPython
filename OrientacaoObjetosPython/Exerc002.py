# criando uma classe
class Carro:
    # variável portas = atributo == 4 
    portas = 4
    # método construtor __init__
    def __init__(self):
        print("Carro criado")


# instanciando o objeto
corolla = Carro()
print("Numero de portas:", corolla.portas)#acessando o atributo portas