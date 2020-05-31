'''
Substituir substring por outra: replace()
recebe dois argumentos.
texto.replace(nova,antiga)
'''
# escreva Pyton eh legal
texto = input("O que acha do curso: " )
print('\n',texto,'\n')
texto=texto.replace('Pyton','Python')
texto=texto.replace('eh','é')
print("Texto corrigido :",texto)