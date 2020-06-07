# Copiar uma Lista em Python

list1 = [1, 2, 3, 4]
# aqui as duas lista estão vinculadas o q mudar em uma vai mudar na outra
list2 = list1
# teste add 0 na list1 e prima list2
list1[0] = 0
print(list2)

#Copiando do Jeito Certo e Difícil
list2 = []
# para copiar corretamente é copiar item por item
for item in list1:
 list2.append(item)
# testanto add -1 a list1 e print list2 e list2
list1[0] = -1
print(list2)
print(list1)

#Copiando do Jeito Certo e Fácil
# concatenar a lista list1 com outra lista (vazia)
list2 = [] + list1
list1[-1] = 5
print(list2)
print(list1)
#Copiando do Jeito Certo e Fácil segunda maneira
list2 = list1.copy()
list1[-1] = 6
print(list2)
print(list1)

