# Elif
# Quando existe a necessidade de avaliar mais de duas possibilidades em um teste condicional.

#if, elif, else
idade = int(input('Informe sua idade: '))
if (idade < 18):
    faixa_etaria = '<18'
elif (idade >= 18 and idade < 30):
    faixa_etaria = '18-29'
elif (idade >= 30 and idade < 40):
    faixa_etaria = '30-39'
else:
    faixa_etaria = '>=40'
print('Se a idade é', idade, 'então a faixa etária é :', faixa_etaria)