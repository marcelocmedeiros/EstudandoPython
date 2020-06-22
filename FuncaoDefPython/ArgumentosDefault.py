# um parâmetro com um valor pré-definido, se o usuário não passar nenhum valor para um parâmetro default ele assume o valor pré definido
# Os argumentos default sempre devem aparecer depois que todos os argumentos posicionais (aqueles que dependem só da posição).

# Programa que calcula a Area e/ou Volume de um retangulo/paralelepípedo

def area(l1, l2, l3=0):
    if l3 == 0:
        area = float(l1) * float(l2)
        print("Área: ", area)
    else:
        volume = float(l1) * float(l2) * float(l3)
        print("Volume: ", volume)

entrada = input("Entre com os lados:")

li = entrada.split()
if len(li) == 2:
    area(li[0], li[1])
else:
    area(li[0], li[1], li[2])