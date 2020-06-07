# Python possui uma função chamada input() que possibilita a entrada de dados via teclado

# Entrada de dados
nome = input("Qual o seu nome?\n") 
print("Hmmm... então você é o famoso " + nome)

# Explicando
# Função input() é chamada, o programa “dá uma paradinha” e fica esperando o usuário digitar alguma coisa. Após o usuário terminar de digitar e teclar Enter, a função retornará o valor introduzido via teclado como uma string.

# "\n" isso significa que vai quabra uma linha (pular p linha debaixo)

# Na segunda linha do programa, o operador + é empregado para concatenar strings, ou seja, para juntar a frase

# Nomes de Variáveis
'''
1- Os nomes podem conter letras, números e o caractere underscore, no entanto não podem ser iniciados por um número. Com relação ao underscore, nós até podemos começar nomes com ele, mas apenas em situações específicas, ver site: https://www.datacamp.com/community/tutorials/role-underscore-python

2- Há diferenciação entre letras maiúsculas e minúsculas, o que significa que se você nomear uma variável como “x”, não poderá referenciá-la como “X” (mas lembre-se de que a recomendação é usar minúsculo nos nomes de todas as variáveis).

3- O nome de uma variável também não pode ser igual ao de uma palavra reservada (keyword) da linguagem Python, cuja lista completa contendo 33 nomes é apresentada abaixo: and; as; assert; break; class; continue; def; del; elif; else; except; False; finally; for; from; global; if; import; in; is; lambda; None; nonlocal; not; or; pass; raise; return; True; try; while; with; yield 
'''

