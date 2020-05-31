'''Programe um script em Python que calcule a média de uma turma, não importa o número
de alunos que ela tenha, seu único script serve para todos os casos'''

alunos = int(input('Quantos alunos tem na turma:'))
soma = 0
n=1
while n <= alunos:
    nota = float(input(f'Digite a nota do {n}° aluno:'))
    n +=1
    soma += nota
media = soma/alunos

print('A média da Turma é', media)