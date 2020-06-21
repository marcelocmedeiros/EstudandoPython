# **kwargs este recurso permite com que você passe um dicionário qualquer como parâmetro de uma função.

# **kwargs
def pessoa(**kwargs):
    for chave, valor in kwargs.items():
        print("{0} = {1}".format(chave,valor))

        
#Sintaxe 1: nome=valor
pessoa(nome='John', profissao='musico')
print("\n")
#Sintaxe 2: passando explicitamente um dicionário (**dicionario)
d={'nome':'Jane','profissao':'escritora','signo':'sagitário'}
pessoa(**d)
print("\n")