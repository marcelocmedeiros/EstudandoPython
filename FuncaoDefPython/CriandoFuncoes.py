# Crie uma função denominada “faixa_etaria”. Esta função recebe como entrada a idade de uma pessoa (número inteiro) e retorna como saída a sua faixa etária (string).

#criando e utilizando uma função
def faixa_etaria(idade):
    if (idade < 18) :
        return '<18'
    elif (idade >= 18 and idade < 30) :
        return '18-29'
    elif (idade >= 30 and idade < 40) :
        return '30-39'
    else :
        return '>=40'


#chamando a função com diferentes valores para o parâmetro "idade"
a = faixa_etaria(15)
b = faixa_etaria(50)
c = faixa_etaria(35)
# o ponto e virgula ";" indica que o print vai pular de linha
print(a); print(b); print(c)