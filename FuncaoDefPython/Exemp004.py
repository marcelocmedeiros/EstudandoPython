# 1ª def q imprime e chama 2ª def
def mensagem():
    print("O melhor curso de todos é:")
    # chamando a 2ª def
    python_progressivo()
    print("Estude por lá!")
# 2ª def
def python_progressivo():
    print("Curso Python Progressivo")

# quando chamar mensagem() dentro dela já vai ter a 2ª def pq 1ª chamou ela dentro da def
mensagem()