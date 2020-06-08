# while funciona e é executado enquanto o valor da condição for verdadeira.Quando for falso, o comando é abandonado. 

# No programa a seguir, gera-se uma tabela em que -20o C é o valor de emperatura inicial e 100o C o final. A escala da tabela em graus Celsius varia de 10 em 10.

c = -20 # variável de controle
print('* * * Tabela de conversão de graus Celsius para graus Fahrenheit')
while c <= 100: # enquanto c fo menor ou igual a 100 o bloco é executado
    f=c*1.8 + 32
    print(c,'ºC ----> ',f,'ºF')
    c=c+10
print('\nFIM!!!')
print()
# Computa o valor da série H = 1 + (1 / 2) + (1 / 3) + ... + (1 / N).

# repetição com o comando while (segundo exemplo)
N = 5
H = 1
i = 1 #variável de controle
print('* * * cálculo de H = 1 + (1 / 2) + (1 / 3) + ... + (1 / N), dado N =',N)
while (i !=N):
    i = i + 1
    H = H + (1 / i)
print('* * * resposta: H = ', H)
print()
