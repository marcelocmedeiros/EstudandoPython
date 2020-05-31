class Carro:
    # passando vários argumentos nome e num
    def __init__(self,nome,num):
        self.nome = nome
        self.portas = num
        print(self.nome,"criado! Ele tem", self.portas,"portas")


palio = Carro("Palio", 2)