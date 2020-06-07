'''
Uma escola te contratou para fazer um software em Python.
Eles querem que você crie um script que exiba o seguinte menu:
0. Sair
1. Exibir lista de alunos com suas notas (cada aluno tem uma nota)
2. Inserir aluno e nota
3. Alterar a nota de um aluno
4. Consultar nota de um aluno específico
5. Apagar um aluno da lista
6. Dar a média da turma
Onde a professora que vai fornecer o nome e nota dos alunos. Quantos ela
quiser. Quantas vezes quiser.
Implemente esse script usando um dicionário
'''

def menu():
    continuar=1
    while continuar:
        continuar = int(input(
        "0. Sair\n"+
        "1. Exibir lista de alunos com suas notas (cada aluno tem uma nota)\n"+
        "2. Inserir aluno e nota\n"+
        "3. Alterar a nota de um aluno\n"+
        "4. Consultar nota de um aluno específico\n"+
        "5. Apagar um aluno da lista\n"+
        "6. Dar a média da turma\n"))
        if continuar==1:
            exibir()
        elif continuar == 2:
            inserir()
        elif continuar == 3:
            alterar()
        elif continuar == 4:
            consultar()
        elif continuar == 5:
            apagar()
        elif continuar == 6:
            media()
        elif continuar == 0:
            print("Encerrando programa")
        else:
            print("Opção inválida")
def exibir():
    # exibir o dicionário, de maneira bonita e padronizada, os nomes e notas dos alunos
    for nome in alunos.keys():
        print("Nome: ", nome, " - Nota: ", alunos[nome])
def inserir():
    # inserindo o nome e a nota 
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Nota dele: "))
    # Se aluno já existir imprime a menssagem
    if alunos.get(nome):
        print("Já existe o aluno ",nome)
    else:
        alunos[nome] = nota
def alterar():
    # altera a nota do aluno 1° informa o nome e depois a nova_nota
    nome = input("Aluno a mudar a nota: ")
    nota = float(input("Nova nota : "))
    # verifica se aluno existe se existir troca o valor da nota
    if nome in alunos.keys():
        alunos[nome] = nota
    # Informar q o aluno não existe no dicionário
    else:
        print("Não existe esse aluno")
def consultar():
    # consulta o aulo e mostra sua nota
    nome = input("Digite o nome do aluno: ")
    # verifica se o aluno existe
    if alunos.get(nome):
        print("Nota de ",nome, ": ", alunos[nome])
    else:
        print("Não existe tal aluno")
def apagar():
    # deleta o aulo do dicionário
    nome = input("Apagar que aluno: ")
    # verifica se o aulo existe dentro do dicionário
    if alunos.get(nome):
        alunos.pop(nome)
    else:
        print("Não existe o aluno ",nome)
def media():
    # faz a média do aluno
    soma = 0
    for count in alunos.values():
        soma += count
    print("Média dos alunos: %.2f" % (soma / len(alunos) ))


alunos = {}
menu()