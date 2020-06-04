# Dicionários

'''
No dicionário abaixo, temos os dados de acesso de 3 usuários, cada um com
seu login e senha, onde o login é a chave e a senha o valor.Faça um script que peça ao usuário seu login e senha, se tiver certo envie
uma mensagem de acesso autorizado, se fornecer a senha errada, informe o
erro.
loginSenha={'joao' : 'rush', 'maria' : 'yes', 'zezinho': 'genesis'}
'''

loginSenha={'joao' : 'rush','maria' : 'yes','zezinho': 'genesis'}
login=input("Qual seu login: ")
senha=input("Senha: ")
if loginSenha[login] == senha:
    print("Acesso autorizado...")
else:
    print("Senha errada")