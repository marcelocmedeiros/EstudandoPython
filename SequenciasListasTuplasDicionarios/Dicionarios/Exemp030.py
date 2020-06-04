# Como Alterar um Item: in mudar o valor de um determinado item
 

notas={'João' : 9,
'Maria' : 10,
'José' : 4 }
nome = input("Aluno a mudar a nota: ")
nota = float(input("Nova nota : "))
# confirmar se item existe | com a instrução in
if nome in notas.keys():
    # se existe ele troca o valor pelo informado
    notas[nome] = nota
else:
    print("Não existe esse aluno")
print(notas)