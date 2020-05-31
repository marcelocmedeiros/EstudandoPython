'''
Você foi contratado por uma escola para fazer o seguinte script em Python:
Primeiro, pergunta a quem vai usar o script quantos alunos tem na sala.
Depois, quantas matérias cada aluno estuda.
Em seguida o usuário vai preenchendo a nota de cada matéria, de cada aluno.
Seu programa deve fornecer a média de cada aluno e a média geral da turma
'''

alunos=int(input("Quantos alunos tem na turma: ") )
materias=int(input("Quantas matérias eles estudam: ") )

mediaTurma=0
#  laço For que vai percorrer os alunos criando 1° divisão
for aluno in range(alunos):
    print("Aluno",aluno+1,":")
    # A cada iteração do Primeiro FOR, antes de digitarmos as notas de cada matéria, devemos zerar essa variável!
    mediaAluno=0
    # outro laço For que vai dar as respectivas notas de cada matéria
    for materia in range(materias):
        print("Nota da materia",materia+1,":", end='')
        nota=int(input())
        # vamos somar nota na variável 'mediaAluno
        mediaAluno += nota
    # para gerar a médio do aluno / var.materias
    mediaAluno /= materias
    print("Media desse aluno:",mediaAluno,"\n")
    # vamos somar mediaAluno na variável 'mediaTurma
    mediaTurma += mediaAluno
# média da Turma soma das médias / var alunos
mediaTurma /= alunos
print("Media da turma:",mediaTurma)