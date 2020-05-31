
import re
'''
A função recompile() do módulo re recebe uma string com sua regex e retorna um objeto do tipo Regex
'''
minhaRegex = re.compile('\\d{4}-\\d{4}')
print(minhaRegex)
'''
Usamos a letra r antes da string no método compile para não precisar fazer "\\"
Para representar uma barra \ em uma string, temos que escapar ela com outra barra: \\
Usando o r, podemos escrever diretamente sem precisa escapar
'''
minhaRegex = re.compile(r'\d{4}-\d{4}')
print(minhaRegex)

