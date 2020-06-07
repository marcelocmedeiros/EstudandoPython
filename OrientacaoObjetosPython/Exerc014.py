# criei a superclasse 
class Veiculo:
    # criei o método construtor dela
    def __init__(self, tipo, modelo, km):
        self.tipo = tipo
        self.modelo = modelo
        self.km = km
# crie a subclasse espcifica 
class Carro (Veiculo):
    # criei o método construtor dela e acresentei portas
    def __init__(self, tipo, modelo, km, portas):
        # informo q classe especifica herda o método e atributos da classe pai    
        Veiculo.__init__(self, tipo, modelo, km)
        self.portas = portas
    # crei um método exibe para imprimir so valores
    def exibe(self):
        print()
        print(self.tipo, "modelo", self.modelo, "com", self.km,"km rodados e", self.portas, "portas.")
        print()

# instanciei o objeto
palio = Carro("Carro", "Palio", "10000", 2)
palio.exibe()
