# *args permite passar um número arbitrário de parâmetros para uma função.
# “*args” pode receber múltiplos parâmetros.
# para a definição de múltiplos parâmetros o que vale mesmo é o *
# poderíamos ter assinado a função como “pessoa(nome, caracteristicas*)”

#P018: *args
def pessoa(nome, *args):
    print("- nome (primeiro parâmetro): ", nome)
    print("- características (outros parâmetros): ")
    for arg in args:
        print("\t",arg) # \t da um TAB 


pessoa('Jane','escritora','sagitariana','romântica')
print("\n")
pessoa('John','músico')
