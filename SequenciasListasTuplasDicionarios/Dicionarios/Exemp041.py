# Alterando o Value 

contatos = {'Yan': '1234-5678', 'Pedro': '9999-9999', 'Ana': '8765-4321',
  'Marina': '8877-7788'}

contatos['Marina'] = '8887-0000'
print(contatos)

contatos = {nome: '9' + contatos[nome] for nome in contatos}
print('#'*10,'Prefixo Add 9','#'*10)
print(contatos)

for nome in contatos:
    contatos[nome] = '(83) ' + contatos[nome]
print('#'*10,'Prefixo Add (83)','#'*10)
print(contatos)
