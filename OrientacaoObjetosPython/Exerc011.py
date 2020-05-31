class Funcionario:
 def __init__(self):
    self.senha = 'senha'

gerente = Funcionario()
print("Senha do gerente:", gerente.senha)
"""
para esconder a senha usamos o atributo privado: __senha, assim 
outros não vêm self.__senha = 'senha' pois programa da erro
"""