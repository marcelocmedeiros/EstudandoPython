#Definição de função que não retorna valor. 


# O exemplo a seguir ilustra um programa Python que possui a declaração da função “imprime_cabecalho()”. Considere que ela seja utilizada para imprimir a string passada em "nome" como o cabeçalho para os relatórios de uma empresa hipotética. Ela não retorna qualquer valor ao ser chamada! Em vez disso, simplesmente executa uma ação: imprimir o cabeçalho.


#função que não retorna valor

def imprime_cabecalho(nome):
    print("\n---------------------------------------")
    print("* * Relatório - " + nome)
    print("---------------------------------------\n")


imprime_cabecalho('Produtos Mais Vendidos')
imprime_cabecalho('Produtos Esgotados')
# verificcando o tipo de classe
print(type(imprime_cabecalho))

# é possível criar funções sem parâmetro
def imprime_cabecalho():
    print("\n---------------------------------------")
    print("* * * *       Relatório         * * * * ")
    print("---------------------------------------\n")


imprime_cabecalho()