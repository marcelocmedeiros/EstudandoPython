# Métodos disponíveis para dicionários

'''
considere que “dic” é um dicionário e “k” uma chave.

    • dic.keys(): retorna uma referência para todas as chaves de “dic”;

    • dic.values(): retorna uma referência para todos os valores de “dic”;

    • dic.items(): retorna um objeto contendo todos os pares {chave:valor} de “dic”;

    • dic.clear(): remove todos os elementos;

    • dic.get(k): recupera o valor do elemento de chave “k”. Se “k” não existir, retorna None;

    • dic.update(d): concatena o conteúdo de um dicionário “d” ao dicionário “dic”.Se algum par “chave:valor” de “d” já existir em “dic”, a informação será sobrescrita.
    
    • del dic[] | dict.pop(): apaga um objeto dentro diciónario.

'''

# Uso de métodos, funções e iteração sobre um dicionário
#(0)-Cria o dicionário (por enquanto sem Belize e Nova Zelândia!)
d = {
'Brasil': 204450649,
'França': 64395345,
'Portugal':10349803,
'México': 127017224,
'Uruguai': 3431555,
}

#(1)-Utilizando os métodos
print('* * * 1-Métodos * * *')
print(d)
print(d.keys())
print(d.values())
print('A população estimada do Brasil é: ', d.get("Brasil"))
print('A população estimada do Brasil é: ', d["Brasil"])
print('----------------------------------------')

#(2)-percorre todos os elementos de "d" a cada iteração, a chave é armazenada em "k" e o valor em "v"
print('* * * 2-Percorrendo o dicionário * * *')
for k, v in d.items():
    print(k, '->', v)

#(3)-Utilizando as funções built-in:

print('----------------------------------------')
print('* * * 3-Usando funções built-in * * *')
print('Total de chaves: ', len(d)) # len(): conta o número de chaves armazenadas no dicionário
print('menor chave: ', min(d)) # min(): menor valor de chave
print('maior chave: ', max(d)) # max(): maior valor de chave

#(4)-Combinando dois dicionários:
print('----------------------------------------')
print('* * * 4-Combinando Dicionários * * *')
d2 = {
'Belize': 179014,
'Nova Zelândia':2213123,
}
d.update(d2)
print('dicionário atualizado: ', d)

#(5)-removendo todos os itens do dicionário
print('----------------------------------------')
print('* * * 5-Destruindo um dicionário * * *')
d.clear()
print(d)

#(6)-apagando um item do dicionário
print('----------------------------------------')
print('* * * 6- Apagando um item do Dicionário * * *')
del d2['Belize']
print(d2)