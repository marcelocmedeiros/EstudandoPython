# FOR ele pode iterar apenas sobre sequências. O FOR para iterar sobre sequências criadas com a função range()

# repetição com for-range()
print('\n* * imprimindo de 0 a 9')
for i in range(10):
    print(i)

print('\n* * imprimindo de 100 a 105')
for i in range(100, 106):
    print(i)

print('\n* * 0 a 15, usando 5 como incremento')
for i in range(0, 16, 5):
    print(i)

print('\n* * ordem reversa: 5, 4, 3, 2, 1')
for i in range(5, 0, -1):
    print(i)

    # Observações: 1- A estrutura for-range() executa um laço por um número fixo de vezes; 2- variável de controle “variável do for”, foi chamada de “i” nos quatro laços implementados. 3- Os limites são definidos com o uso da função range(inicio, fim e incremento)

# Sintaxe range(inicio, fim, incremento)                                    Inicio ->  é opcional|caso seja omitido seu valor inicial = 0.                  Fim ->      é obrigatório | a sequência será gerada até ele.                Incremento -> é opicional|caso seja omitido seu valor inicial =1.

    # 2- Observação:                                                            1º) Todos os parâmetros devem ser do tipo inteiro;                          2º)Todos os parâmetros podem ser positivos ou negativos;                    3º) Na função range() o conjuntos de valores são indexados a partir do valor 0 e não do valor 1. Em outras palavras: o primeiro elemento de uma sequência, lista, vetor, etc., sempre possuirá o índice 0. É por isso que o comando range(n) produz uma lista cujo primeiro elemento é 0 e o último n-1,• Exemplos: ◦ range(3) #[0,1,2] ◦ range(1,4) #[1,2,3] ◦ range(0,10,2) #[0,2,4,6,8]               