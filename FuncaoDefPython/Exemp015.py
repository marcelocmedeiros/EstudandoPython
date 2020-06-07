def par(x):
    # recebe x=num e testa
    if (x%2)==0:
        return True
    else:
        return False


while True:
    num = int(input("Insira um número: "))
    # quando informa o num if chama def par(num)
    if par(num):
        # se for True é par se não ímpar
        print("É par")
    else:
        print("É ímpar")