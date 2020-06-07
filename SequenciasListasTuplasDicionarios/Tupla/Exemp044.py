# Os operadores * (repetição), + (concatenação), in (teste de pertinência) também funcionam para tuplas, assim como as funções len(), min(), max() e sum().

# * (repetição)
tupla = ('a', 'b', 'c', 'd', 'e')
print((tupla)*3)

# + (concatenação)
tupla = ('a', 'b', 'c', 'd', 'e')
tupla = ('A',) + tupla[1:]
print(tupla)

# in (teste de pertinência)
tupla1 = (10, 20, 30, 40, 50)

print(57 in tupla1)# retorna False 
print(50 in tupla1)# retorna True

# funções len(), min(), max() e sum()
tupla1 = (10, 20, 30, 40, 50)

print(len(tupla1))
print(min(tupla1))
print(max(tupla1))
print(sum(tupla1))
