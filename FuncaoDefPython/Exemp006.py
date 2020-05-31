def teste():
    banda="Rush"
    # 1 executa o print
    print("A melhor banda do mundo é ", banda)
    # agora chama teste2
    teste2()
def teste2():
    banda="Beatles"
    # dentro de teste2 1 executa o print
    print("A melhor banda do mundo é ", banda)
    # depois chama teste3
    teste3()
def teste3():
    banda="Iron Maiden"
    # e quando chama teste3 este só executa o print
    print("A melhor banda do mundo é ", banda)


teste()