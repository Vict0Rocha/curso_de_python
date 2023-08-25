"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Victor Hugo'
valor = 500.292925
variavel = '%s, o preço é R$%.2f' % (nome, valor)
print(variavel)

print('O hexadecimal de %d é %05X' % (81815,8115151))