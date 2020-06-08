# Funções pré-definidas que podem ser usadas em listas
'''
• sum(lst): soma os elementos da lista (apenas para listas com elementos numéricos);
• min(lst), max(lst): retornam, respectivamente o menor e o maior valor de “lst” (para qualquer tipo de lista);
• len(lst): retorna o tamanho da lista.
'''
# Aplicando funções pré-definidas sobre listas
lst_qi = [126, 100, 130, 92, 120, 99, 125, 72]

print("resultados do teste de QI: ", lst_qi)
print("maior: ", max(lst_qi))
print("menor: ", min(lst_qi))
print("soma: ", sum(lst_qi))
print("media: ", sum(lst_qi) / len(lst_qi))

# Comparação de Listas

[1,2,3] > [1, 5, 10] #retorna False
[20] > [10, 998, 800] #retorna True

'''
A comparação começa pelo primeiro primeiro elemento de cada sequência. Se eles forem iguais, o segundo elemento será comparado e assim por diante, até que
elementos diferentes sejam encontrados. Elementos subsequentes são ignorados.
'''