# Métodos disponíveis para dicionários
"""
• dic.keys(): retorna uma referência para todas as chaves de “dic”;

• dic.values(): retorna uma referência para todos os valores de “dic”;

• dic.items(): retorna um objeto contendo todos os pares {chave:valor} de “dic”;

• dic.clear(): remove todos os elementos;

• dic.get(k): recupera o valor do elemento de chave “k”. Se “k” não existir, retorna None;

• dic.update(d): concatena o conteúdo de um dicionário “d” ao dicionário “dic”. Se algum par “chave:valor” de “d” já existir em “dic”, a informação será sobrescrita.
"""

# uso de métodos, funções e iteração sobre um dicionário
# Cria o dicionário (por enquanto sem Belize e Nova Zelândia!)
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
print(d.keys()) # dic.keys(): retorna chaves
print(d.values()) # dic.values(): retorna valores das chaves
# dic.get(k): recupera o valor do elemento de chave “k”. Se “k” não existir, retorna None
print('A população estimada do Brasil é: ', d.get("Brasil"))
