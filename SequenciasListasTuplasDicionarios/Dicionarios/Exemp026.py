# Como verificar se uma chave existe: Método get()

'''
o método get()
Recebe dois parâmetros: get(key, value)
    • key - É a chave que você quer testar, pra saber se existe
    • value - Caso essa chave não existe, ele retorna esse valor ou None
(caso não forneça nada, é opcional esse value)
'''

notas={'João' : 9,
'Maria' : 10,
'José': 4}
if notas.get('Peart') == None:
    print("Não existe aluno Peart")
else:
    print("Aluno existente")

# se key não existir retorna None
print(notas.get('Peart'))

