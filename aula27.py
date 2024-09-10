"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[4:8:2]) //4 = número do inicio : 8= número final : 2 é a quantidade de casas andadas
print(variavel[::-1])