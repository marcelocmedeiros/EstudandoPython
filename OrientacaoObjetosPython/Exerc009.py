# importando a biblioteca random gerar n° aleatórios
import random
# cria minha classe CaraCoroa
class CaraCoroa:
    # criei meu método construtor
    def __init__(self):
        # inicia-se com "cara"
        self.lado = 'Cara'

    # criei o mpetodo para lançar moeda
    def lancar(self):
        # usei if/else para consdições de lançamento da moeda
        if (random.randint(0,1))%2==0: 
        # random.randint(0,1) p gera sempre n° aleatório
            self.lado = 'Cara'# se ==0 lado = Cara
        else:
            self.lado = 'Coroa'# se não lado = coroa
        # retorno o lado
        return self.lado


# instanciando o objeto
moeda = CaraCoroa()
op=1
# loop infinito p o jogador
while op:
    # se escolher 0 sai do jogo
    op=int(input("0.Sair\n"
    "1.Jogar de novo\n"
    "Qual é sua opção: "))
    # toda vez q opção = 1 imprime o lançamento
    if op:
        print(moeda.lancar())