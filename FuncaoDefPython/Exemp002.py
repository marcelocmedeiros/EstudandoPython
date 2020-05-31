# cabeçalho da def soma()
def soma():
    # chamo dois números
    x = float(input('Primeiro numero:'))
    y = float(input('Segundo numero:'))
    # código soma
    soma = x + y
    print("Soma:", soma)
# variável continuar controla o loop quando ela =1 ou qualquer outro número == True
continuar=1
# o loop é executado e cai no IF que chama a função soma()
while continuar:
    # executa novamente a função soma()
    if(continuar):
        soma()
    # para o loop parar continuar tem que receber 0 == False
    continuar=int(input('Digite 0 se deseja encerrar ou qualquer outro número para continuar:'))