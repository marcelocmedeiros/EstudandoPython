'''
Crie um programa que exiba todos os segundos e minutos no intervalo de uma hora,
no seguinte formato: XXmin YYs. Por exemplo: 12min59s
'''

for minutos in range(60):
    for segundos in range(60):
        print(minutos,'min', segundos,'s')

