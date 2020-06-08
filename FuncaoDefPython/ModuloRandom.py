# funções para a geração de números aleatórios
'''
    • random.random() : retorna um número real (float) na faixa [0.0, 1.0). Esta notação indica que 0.0 pode ser gerado, mas 1.0 não;
    • random.randint(inicio,fim) : retorna um número inteiro na faixa [inicio, fim);
    • random.choice(sequência) : sorteia um elemento de uma sequência;
'''

# Exemplifica o uso das funções do módulo 'random'. Preste especial atenção na receita que deve ser utilizada para trabalhar com sementes.
# módulo ‘random’
import random
#(1)-função randint()
for i in range(6):
    n = random.randint(1,61) 
    print(n)
#(2)-função choice()
k = random.choice([1,2,3,4,5])
print("\n", k)