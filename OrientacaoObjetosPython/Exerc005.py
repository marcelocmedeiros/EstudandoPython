# criando uma classe
class Carro:
    # variável portas = atributo == 2
    portas = 2
    # método construtor __init__
    def __init__(self):
        print("Carro criado")
    
    # criando métododefinePortas
    def definePortas(self, num):
        self.portas = num
    
    # criando método exibePortas
    def exibePortas(self):
        return self.portas

# instanciando o objeto
carro = Carro()
# num = recebe o n° de portas
num=int(input("Numero de portas:"))
# chamou método definePortas
carro.definePortas(num)
# chamando o método exibePortas
print("Numero de portas:", carro.exibePortas())