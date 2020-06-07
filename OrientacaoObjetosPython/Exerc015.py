#criando a superclasse
class Conta:
    def __init__(self):
        self.saldo = 0
    # método getSaldo
    def getSaldo(self):
        # retorn = 0
        return self.saldo
# 1ª subclasse pessoa fisica
class PF (Conta):
    def __init__(self,):
        Conta.__init__(self)
    # método que cobra 5 reias por operação
    def setSaldo(self, valor):
        # retira de cada operação -5 reais
        self.saldo += valor - 5
# 2ª subclasse pessoa juridica
class PJ (Conta):
    def __init__(self):
        Conta.__init__(self)
    # método que cobra 10 reias por operação
    def setSaldo(self, valor):
        # retira de cada operação -10 reais
        self.saldo += valor - 10

# pergunta qual tipo de conta quer criar 
print("1.Criar conta Pessoa Física")
print("2.Criar conta Pessoa Jurídica")
op = int(input("Opção:"))
# condições da opção escolhida antes
if op==1:
    conta = PF()
elif op==2:
    conta = PJ()
# loop infinito p as opções do caixa
while True:
    print("1. Ver saldo")
    print("2. Sacar / Depositar")
    op = int(input("Opção:"))
    # opções esolheidas antes
    if op == 1:
        print("R$", conta.getSaldo())
    elif op==2:
        val = float(input("Valor para movimentar:"))
        conta.setSaldo(val)