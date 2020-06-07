'''
Faça um script que peça ao usuário o número de matérias da escola, ou
seja, um inteiro positivo.
Em seguida, ele vai digitando o valor de cada nota, de cada matéria e isso
será armazenado numa lista.
Ao final, seu script deverá fornecer a média geral do aluno
'''
n = int(input("Numero de materias: "))
notas = []
soma=0

for count in range(n):
    nota=float(input("Nota da materia %d°: " % (count+1)))
    notas += [nota]
    soma += nota
print("Notas: ",notas)
print("Media: %.2f" % (soma/n))