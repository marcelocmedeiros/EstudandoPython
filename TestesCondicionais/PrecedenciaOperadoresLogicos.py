"""
  Operador | Ordem de avaliação
    not         1
    and         2
    or          3
"""

preco = 999.99; categoria = 'B'
if categoria=='B' or categoria=='A' and preco < 500:
    print('1º condição: selecionado')
else:
    print('não selecionado')
# onde os parênteses são empregados para alterar a precedência do teste
if (categoria=='B' or categoria=='A') and preco < 500:
    print('selecionado')
else:
    print('2º condição: não selecionado')
