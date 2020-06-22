# Se quisermos manter a nossa lista original a seguinte sintaxe: funcao(lista[:])

def altera(li):
    lista_alterada = li
    for i in range(0, 3):
        li[i] = 'alterado'
    return lista_alterada


lista = ['Paula', 'Raquel', 'Lucia', 'Ana', 'Maria']
print('Lista antes da função:')
print(lista)

altera(lista[:])
print()
print('Lista depois da função:')
print(lista)
print('\nCopia da lista dentro da função:')
print(altera(lista[:]))
print()