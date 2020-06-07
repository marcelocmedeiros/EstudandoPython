# variável global fora do escopo da def
desc = 10

def desconto(valor):
    # chamo var global
    global desc
    # código da def
    print("Preço original : R$ ",valor)
    print("Desconto : ", desc,"%")
    desc /= 100
    print("Valor desconto : ", valor*desc)
    print("Preço c/ desconto: ", valor*(1-desc) )

#prog pric pede valor do produto
val = float(input("Preço do produto: "))
#chamo a def desconto
desconto(val)