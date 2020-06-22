# Programa que calcula a área de um retângulo, círculo ou triângulo
# Modificamos o programa area.py para usar funções lambda

retangulo = lambda lado_a, lado_b: lado_a * lado_b
triangulo = lambda lado, altura: (lado * altura) / 2
circulo = lambda raio: 3.14 * (raio ** 2)

opcao = -1
while opcao != 0:
    print('Escolha o objeto que deseja calcular a área')
    print()
    print('1 - Retângulo')
    print('2 - Triângulo')
    print('3 - Círculo')
    print('0 - Sair')
    print()
    opcao = int(input('Entre com o número da opção desejada: '))
    if (opcao == 1):
        lado_a = float(input('Entre com um lado do retângulo: '))
        lado_b = float(input('Entre com o outro lado do retângulo: '))
        print('\nA área do retâgulo é: {0:.2f}'.format(retangulo(lado_a, lado_b)))
    elif (opcao == 2):
        lado = float(input('Entre com o lado do triângulo: '))
        altura = float(input('Entre com a altura do triângulo: '))
        print('\nA área do triângulo é: {0:.2f}'.format(triangulo(lado, altura)))
    elif (opcao == 3):
        raio = float(input('Entre com o raio do cículo: '))
        print('\nA área do círculo é: {0:.2f}'.format(circulo(raio)))
    elif (opcao != 0):
        print('\n{0} não é uma opção valida'.format(opcao))

    print()
print('Volte a qualquer hora')