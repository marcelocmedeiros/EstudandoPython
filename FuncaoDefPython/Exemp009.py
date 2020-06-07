# função 2 parametros
def conta_caractere(texto,char):
    # código count conta quanta letra "x" tem no texto
    count = 0
    # laço for onde letra vai percorrer texto
    for letra in texto:
        # se letra estiver em texto
        if letra == char:
            # soma +1 a count
            count += 1
    print("A letra", char,"apareceu",count,"vezes na string")

# prog pricipal pede para digitar um texto e depois uma letra
string=input("Digite um texto qualquer: ")
caractere = input("Digite um caractere: ")
# chamo a def com 2 argumentos string,caractere
conta_caractere(string,caractere)