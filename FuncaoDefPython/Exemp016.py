# retornando mais de um valor

def cadastro():
    name = input("Qual seu nome: ")
    age = int(input("Idade: ") )
    # retorna para quem chamou a def 2 valores tem que separá-los por virgulas
    return name, age


print("Iniciando cadastro...")
# vai receber duas informações depois de chamar cadastro()
nome, idade = cadastro()
print("Cadastro realizado com sucesso:")
print("Seu nome é", nome, "e você tem", idade,"anos de idade.")