
def soma():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("Soma: ",x+y)
def subtracao():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("Subtracao: ",x-y)
def multiplicacao():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("Multiplicacao: ",x*y)
def divisao():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("Divisao: ",x/y)
# variável opçao inicia o loop quando ela =1 ou qualquer outro número == True
opcao=1
# o loop é executado e para escolha de uma das opções
while opcao:
    print("0. Sair")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicação")
    print("4. Divisão ")
    # para o loop parar tem que receber 0 == False
    opcao = int(input("Opção: ")) # escolha opcao
    # cai no IF e chama a função que foi escolhida
    if(opcao==1):
        soma()
    if(opcao==2):
        subtracao()
    if(opcao==3):
        multiplicacao()
    if(opcao==4):
        divisao()