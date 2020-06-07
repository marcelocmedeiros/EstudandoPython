# criei a classe Funcionário
class Funcionario:
    # criei método construtor p funcionário
    def __init__(self, nome):
        # # atributo privado __nome
        self.__nome = nome
    # método retornaNome p devolver nome do funcionário
    def retornaNome(self):
        return self.__nome
#cirei 2ª classe agora p empresa
class Empresa:
    # criei uma lista q vai armazenar funcionários
    func = []
    # criei método construtor p empresa
    def __init__(self):
        print('=-'*10)
        print("Empresa Tabajara em funcionamento")
        print('=-'*10)
        # loop infinito para sempre poder contratar 
        while True:
            # opções iniciais do programa
            print("1. Contratar")
            print("2. Exibir lista de funcionarios")
            op=int( input("O que você deseja fazer: ") )
            # condição 1 p exibir e 2 p contratar
            if op==1:
                # chama o método contratar
                self.contratar()
            elif op==2:
                # chama list de funcionários
                self.exibir()
            # caso digite outra opção que não 1 ou 2
            else:
                print("Opçao invalida")
    # método contratar
    def contratar(self):
        # nome = o nome do contratado
        nome = input("Nome: ")
        # add lista de funcionários
        self.func.append( Funcionario(nome) )
    # método exibir
    def exibir(self):
        # mostra a lista de funcionário um por um 
        for funcionario in self.func:
            print(funcionario.retornaNome())
# instanciar o objeto empresa
Empresa()