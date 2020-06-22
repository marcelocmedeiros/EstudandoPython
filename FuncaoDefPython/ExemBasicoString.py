'''
Em Python também podemos retornar uma coleção de valores como uma lista, tupla ou dicionário.
No programa conta_palavras.py abaixo e pedido que o usuário entre com uma frase ou texto e
retorna um conjunto contendo as palavras do texto como chaves e o valor como a frequência que
as palavras aparecem no texto
'''

# Programa que cria uma conjunto com as palavras como chave
# e o valor como a frequência que essas palavras aparecem no texto

def conta_palavras(texto):
    """Conta a frequência das palavras em um texto"""

    # Separa o texto em palavras
    palavras = texto.split()

    # Cria um dicionario onde as chaves são a palavras e valor é a frequência
    f = {}
    for palavra in palavras:
        # Coloca a palavra em letras minusculas para não existir diferenciação entre maiuscula e minusculas
        palavra = palavra.lower()

        # Verifica se a palavra já é uma chave do dicionario
        # se for soma mais um a sua frequencia
        # se não for insere a palavra como chave com o valor um
        if palavra in f:
            f[palavra] += 1
        else:
            f[palavra] = 1

    return f

texto = input("Entre com uma frase: ")
print(conta_palavras(texto))

