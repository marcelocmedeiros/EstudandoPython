# importando a biblioteca random gerar n° aleatórios
import random
# cria minha classe CaraCoroa
class CaraCoroa:
    # criei meu método construtor
    def __init__(self):
        # inicia-se com "cara"
        self.lado = 'Cara'
    # criei o método para lançar moeda
    def lancar(self):
        # usei if/else para consdições de lançamento da moeda
        if (random.randint(0,1))%2==0:
            # random.randint(0,1) p gera sempre n° aleatório
            self.lado = 'Cara'# se ==0 lado = Cara
        else:
            self.lado = 'Coroa'# se não lado = coroa
        # retorno o lado
        return self.lado
# cria minha 2ª classe Dado
class Dado:
    # criei 2º método construtor
    def __init__(self):
        # inicialmente = 1
        self.lado = 1
    # criei o método para lançar o dado
    def lancar(self):
        # return c/ random.randint(1,6) retorna um n° aleatório (1,6)
        return random.randint(1,6)

# instanciando os objetos
moeda = CaraCoroa()
dado = Dado()

op=1
# loop infinito p o jogador
while op:
    # se escolher 0 sai do jogo
    op=int(input("0.Sair\n"
    "1.Lançar Moeda\n"
    "2.Lançar dado\n"
    "Qual é sua opção: "))
    # toda vez q opção = 1 imprime o lançamento da moeda
    if op==1:
        print(moeda.lancar())
    # toda vez q opção = 2 imprime o lançamento dao dado
    elif op==2:
        print(dado.lancar())