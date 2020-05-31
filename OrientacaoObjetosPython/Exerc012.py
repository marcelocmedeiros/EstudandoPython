# criei a classe Funcionário
class Funcionario:
    # contador
    count = 0
    # criei um método construtor
    def __init__(self, nome):
        # atributo privado __nome
        self.__nome = nome
        print('=-'*10)
        print(nome, "contratado!")
        # Atributo de classe vão atuar numa mesma variável
        Funcionario.count +=1
        print('=-'*10)
        print("Número de funcionarios:", Funcionario.count)
        print('=-'*10)
op=1
#lista de funcionários
func = []
# loop infinito para add funcionários
while op:
    # 0 sair do programa 1 add funcionário
    op=int(input("0. Sair\n1. Criar funcionario\nO que você quer fazer:"))
    # condição p prog add funcionário
    if op==1:
        print('=-'*10)
        nome = input("Nome: ")
        func.append( Funcionario(nome) )
