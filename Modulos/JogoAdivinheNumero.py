"""
Crie um jogo em Python onde o computador vai sortear um número de 1 até
100.
Em seguida, você vai tentar adivinhar que número foi esse.
A cada tentativa, ele vai te dizer se seu palpite foi alto, baixo ou se você
acertou.
Quando acertar, deve mostrar quantas tentativas você fez até acertar
"""
# bibliotera q gera n° aleatórios
from random import randint
# função gera q sorteia 1-100
def gera():
    return randint(1,100)

# função game q controla o jogo
def game():
    # armazena a número regado da def gera()
    resposta = gera()
    # soma total de tentativas
    tentativa = 0
    print("\nPalpite gerado!")

    chute=0
    # loop infinito até chute != resposta
    while chute is not resposta:
        # somatório para cada loop
        tentativa +=1
        chute = int(input("Qual seu chute: "))
        if chute > resposta:
            print("Errou! É um valor menor que ", chute)
        elif chute < resposta:
            print("Errou! É um valor maior que ", chute)
        else:
            print("Parabéns! O número gerado foi ",resposta, \
            "Acertou em ",tentativa," tentativas!")

# loop para sempre jogar mesmo quando jogador certar
while True:
    game()