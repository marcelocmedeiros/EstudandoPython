# uso de métodos, funções e iteração sobre um dicionário
# Cria o dicionário (por enquanto sem Belize e Nova Zelândia!)
d = {
'Brasil': 204450649,
'França': 64395345,
'Portugal':10349803,
'México': 127017224,
'Uruguai': 3431555,
}
#(4)-Combinando dois dicionários:
print('----------------------------------------')
print('* * * 4-Combinando Dicionários * * *')
d2 = {
'Belize': 179014,
'Nova Zelândia':2213123,
}
# dic.update(d): concatena o conteúdo de um dicionário “d” ao dicionário “d2”
d.update(d2)
print('dicionário atualizado: ', d)