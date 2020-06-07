# trata-se de constante global é uma constante pq não tem keyword global dentro da def
# assim ela pode ser usada por todas as def vista por todos, mas não pode ser alterada
pi = 3.14

def perimetro(raio):
    print("Perimetro: ", 2*pi*raio)
    def area(raio):
        print("Área: ", pi*raio*raio)


raio = float(input("Raio do círculo: "))#perimetro(raio)
perimetro(raio)