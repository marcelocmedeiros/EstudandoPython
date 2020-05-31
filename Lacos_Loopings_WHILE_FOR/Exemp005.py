'''
"Programe um script em Python que calcule a média de uma turma, não
importa o número de alunos que ela tenha, seu único script serve para
todos os casos"
'''
senha = "2112" # esta lendo como string

tentativa = input('Digite sua senha:') # está recebendo como string

while (senha != tentativa): # True enquanto senha for diferente de tentativa
    print("Senha Incorreta! Tente novamente!")
    tentativa = input('Digite sua senha:')

print("Senha correta. Entrando no sistema...") # print fora do laço p ser impresso quando while for False
