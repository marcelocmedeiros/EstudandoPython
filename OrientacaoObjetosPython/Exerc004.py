# criando uma classe
class Carro:
    # variável portas = atributo == 2
    portas = 2
    # método construtor __init__
    def __init__(self):
        print("Carro criado")
    
    # criando métododefinePortas
    def definePortas(self):
        # num vai receber o n° de portas
        num=int(input("Numero de portas:"))
        # num recebe um valor q depois atribui a variável portas
        self.portas = num
    
    # criando método exibePortas
    def exibePortas(self):
        # retorna o atributo portas
        return self.portas


# instanciando o objeto
carro = Carro()
# chamou método definePortas
carro.definePortas()    
# chamando o método exibePortas
print("Numero de portas:", carro.exibePortas())