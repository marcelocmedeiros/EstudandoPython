# criando uma classe
class Carro:
    # variável portas = atributo == 3
    portas = 3
    # método construtor __init__
    def __init__(self):
        print("Carro criado")
    
    # criando método exibePortas
    def exibePortas(self):
        # retorna o atributo 3
        return self.portas


# instanciando o objeto
veloster = Carro()
print("Numero de portas:",veloster.exibePortas())# chamando o método exibePortas
