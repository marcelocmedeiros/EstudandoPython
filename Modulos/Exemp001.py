import calculadora

while True:
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    op=int(input("Que operação deseja realizar: "))
    if op==1:
        x = float(input("Primeiro numero: "))
        y = float(input("Segundo numero: "))
        print("Soma:", calculadora.soma(x,y))
    elif op==2:
        x = float(input("Primeiro numero: "))
        y = float(input("Segundo numero: "))
        print("Subtração:", calculadora.subtracao(x,y))
    elif op==3:
        x = float(input("Primeiro numero: "))
        y = float(input("Segundo numero: "))
        print("Multiplicação:", calculadora.multiplicacao(x,y))
    elif op==4:
        x = float(input("Primeiro numero: "))
        y = float(input("Segundo numero: "))
        print("Divisão:", calculadora.divisao(x,y))
    else:
        print("Opção inválida,tente novamente")
