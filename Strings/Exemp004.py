''' concatenar String operador +'''

texto = "Curso"
print(texto,end='')# usando end='' para unir duas linhas de print

texto1 = " de "
print(texto1,"\n")# usando caracter "\n" para pula uma linha no print

texto = texto + " Python"
print(texto,"\n")

texto = texto + texto1 + " Python"
print(texto)
