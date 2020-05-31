def teste():
    print("Estamos dentro da função!")
    var=2112
    # aqui var é impresso pq esta dentro da  função e ela é uma varável local
    print("Valor de var:",var)

teste()
print("Agora estamos fora da função!")
# Aqui var não é impresa pq ela não existe fora da função e código da erro 'var' is not defined
print("Valor de var:",var)