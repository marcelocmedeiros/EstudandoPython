# Definir o valor de uma chave:Método setdefault()

'''
o método setdefault(key, value)
testa se tem key, se não tiver ele cria um item com
esta key e dá o valor 8 para ele.
'''
# caso key exista ela permanece com o valor a ela atribuido no dicionário
notas={'João' : 9,
'Maria' : 10,
'José': 4,}
notas.setdefault('Peart', 8)
print(notas)

