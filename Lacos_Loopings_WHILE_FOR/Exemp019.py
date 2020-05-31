'''
Faça o mesmo do exemplo anterior, mas adicione as horas para ficar no
formato: XXh YYmin ZZs
'''
for horas in range(24):
    for minutos in range(60):
        for segundos in range(60):
            print(horas,'h',minutos,'min', segundos,'s')
