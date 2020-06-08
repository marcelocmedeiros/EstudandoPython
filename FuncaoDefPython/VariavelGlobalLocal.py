# variável global, pois é uma variável declarada no corpo do programa principal. Uma variável declarada dentro de uma função é, por sua vez, chamada de variável local.

# Passagem de parâmetro – variável de tipo primitivo
def soma_um(numero):
    numero=numero+1
    print("somei um dentro da função: ", numero) # processado dentro da def


k=100
print('valor original de k:', k) # antes de ir para def
soma_um(k) # enviado para def 
print('Terminou a função e k, na verdade, não mudou:', k) # depois de processado dentro da def

# note que o k = 100 continuou o mesmo, pois estava decladaro fora da def.