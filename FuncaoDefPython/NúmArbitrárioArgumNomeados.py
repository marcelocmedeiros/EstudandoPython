# Caso precisemos passar um número arbitrário de argumentos nomeados para uma função podemos usar dois asteriscos (**) antes do parâmetro que irá receber esses argumentos. Esse parâmetro funciona como um dicionário de argumentos.

# Programa procurado

def descricao(cor, sexo, altura, olhos, **descricao):
    print('Descrição:')
    print('cor:', cor)
    print('altura:', altura)
    print('cor dos olhos:', olhos)
    for k in descricao:
        print('{0}: {1}'.format(k, descricao[k]))

    print()


descricao('branca', 'masculino', 1.70, 'castanhos',
          cicatriz='no rosto', tatuagem='estrela na mão direita')
descricao('parda', 'feminino', 1.54, 'verdes',
          tatuagem='pantera no ombro esquerdo', cabelo='pintado de azul')
