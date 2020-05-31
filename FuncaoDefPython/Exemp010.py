def muda(var):
    # var variável local só vista dentro da funça
    var=0
    print("Valor de x dentro da função: ",var)

# variávelde escopo geral
var=1
print("Valor de x antes da função: ",var)
# chamou a def var
muda(var)
print("Valor de x ao sair da função: ",var)