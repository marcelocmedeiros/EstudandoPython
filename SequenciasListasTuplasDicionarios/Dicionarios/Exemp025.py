# Exibindo Corretamente um Dicionário

notas={'João' : 9,
'Maria' : 10,
'José': 4}
# Pegamos a variável nome e usar ela pra acessar os valores corretos do dicionário
for nome in notas.keys():
    print(nome," tirou nota: ", notas[nome])