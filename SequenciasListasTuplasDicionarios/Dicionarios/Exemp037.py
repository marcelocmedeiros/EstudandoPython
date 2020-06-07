# uso de métodos, funções e iteração sobre um dicionário
# Cria o dicionário (por enquanto sem Belize e Nova Zelândia!)
d = {
'Brasil': 204450649,
'França': 64395345,
'Portugal':10349803,
'México': 127017224,
'Uruguai': 3431555,
}

#(2)-percorre todos os elementos de "d"
# a cada iteração, a chave é armazenada em "k" e o valor em "v"
print('----------------------------------------')
print('* * * 2-Percorrendo o dicionário * * *')
# dic.items(): retorna um objeto contendo todos os pares {chave:valor} de “dic”
for k, v in d.items():
    print(k, '->', v)