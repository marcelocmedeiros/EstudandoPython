# Adicionar item em um Dicionário

#o método notas.get(nome) com este método podemos chegar se a key já existe
# se key não existe ele atribui a key e o valor juntos ao dicionário

notas={'João' : 9,
'Maria' : 10,
'José' : 4}
nome = input("Digite o nome do aluno: ")
nota = float(input("Nota dele: "))
# se key já existir ele informa e não altera nada
if notas.get(nome):
    print("Ja existe o aluno ",nome)
# cria key e values
else:
    notas[nome] = nota
print(notas)

