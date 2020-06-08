# O comando break quebrar um laço “na marra”, passando o fluxo de execução do programa para a linha que estiver localizada imediatamente depois do fim do bloco de comandos do laço. 
# O comando continue quebrar uma iteração, mas não o laço propriamente dito. o continue é executado, o fluxo de execução do programa é automaticamente desviado para a linha que contém o comando while.

# while com break + while com continue
print('-------------------------------------')
print('1-Exemplo de while com break:\n')
n=-1;
while (n < 21):
    n=n+1;
    if n%2 != 0: break #quebra o laço se n for ímpar...
    print(n)
print('fim do while com break...\n')
print('-------------------------------------')
print('2-Exemplo de while com continue:\n')
n=-1;
while (n < 21):
    n=n+1;
    if n%2 != 0: continue #quebra a iteração se n for ímpar...
    print(n)
print('fim do while com continue...\n')