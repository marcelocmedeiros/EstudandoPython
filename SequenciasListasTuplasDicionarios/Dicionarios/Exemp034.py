# Como Copiar um Dicionário ou Lista

# Cópia profunda (deep copy): copy.deepcopy()

# importando módulo copy 
import copy

login={'joao' : 'senha',
'maria' : '123456',
'zezinho': 'restart'}
backup = copy.deepcopy(login)
print(backup)
login['zezinho'] = 'ironmaiden'
print(login)
print(backup)
