# criando uma classe
class Conta:
    #variável saldo = atributo == 0.0
    saldo = 0.0
    # método construtor __init__
    def __init__(self):
        print("Conta do cliente criada")
    # criando método depositar
    def depositar(self, num):
        #condição para o deposito
        if(num>0):
            self.saldo += num
        else:
            print("Nao é possível depositar 0 ou menos")
    
     # criando método sacar
    def sacar(self, valor):
        #condição para o saque
        if(valor<=self.saldo):
            self.saldo -= valor
        else:
            print("Valor insuficiente. Você tem:", self.saldo)
    
     # criando método exibeSaldo
    def exibeSaldo(self):
        return self.saldo

# instanciando o objeto
pessoa = Conta()

op = True
# loop infinito mostrando o o cliente deseja fazer
while op:
    print("0. Sair")
    print("1. Exibir saldo")
    print("2. Depositar")
    print("3. Sacar")
    op=int(input("Informe o que deseja fazer: "))
    # if elif e else para as opções do cliente
    if(op==1):
        print("Saldo:", pessoa.saldo)
    elif(op==2):
        num=float(input("Valor para depositar:"))
        pessoa.depositar(num)
    elif(op==3):
        num=float(input("Valor para sacar:"))
        pessoa.sacar(num)
    else:
        print("Saindo do sistema...")