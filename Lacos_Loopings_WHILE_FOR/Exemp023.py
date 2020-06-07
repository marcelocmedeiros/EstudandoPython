# Python List Comprehensions

compressao = [ x ** 2 for x in range(10)]
print(compressao)

compressao = [ 'a' * x for x in range(10)]
print(compressao)
compressao = [ sum(range(0,x+1)) for x in range(10) ]
print(compressao)
compressao = [ x for x in range(20) if x % 2 == 0 ]
print(compressao)