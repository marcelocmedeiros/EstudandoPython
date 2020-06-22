# Funções lambda são funções anonimas de uma única linha que aceitam argumentos.

# Programa para converter temperatura de Fahrenheit para Celsius

temp_celsius = lambda f: (5/9) * (f - 32)

f = float(input('Entre com a temperatura em Fahrenheit: '))
print('A temperatura em Celsius é: {0:.2f}'.format(temp_celsius(f)))
