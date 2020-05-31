'''
Gerar Números Aleatórios em Python - A Biblioteca random
'''
"""
Crie um programa em Python que simula o resultado de um dado, ou seja,
gera números aleatórios de 1 até 6, quantas vezes o usuário desejar.
"""
# importando a biblioteca random
import random
#
continuar=1
# loop infinito enquanto continuar receber n° != 0
while continuar:
    # dentro do print chamei random.randint(1,6) que gera número aleatórios
    print("Número aleatório gerado:", random.randint(1,6))
    continuar=int(input("Gerar novamente?\n1.Sim\n0.Não\nResposta:"))
