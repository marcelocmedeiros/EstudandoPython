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
            self.saldo = num
        else:
            print("Nao é possível depositar 0 ou menos")
        
    # criando método exibeSaldo
    def exibeSaldo(self):
        return self.saldo

# instanciando o objeto
pessoa = Conta()
# imprime o saldo inicial
print("Saldo inicial:", pessoa.saldo)
# pede o valor do deposito
num = int(input("Depositar:"))
# mostra o saldo final
pessoa.depositar(num)
print("Saldo atual:", pessoa.saldo)