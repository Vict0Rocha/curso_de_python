"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
n = input('Digite um valor <<< ')

try:
    n_float = float(n)
    print(f'O dobro de {n_float} é {n_float * 2:.2f}')
except:
    print('Isso não é um némro! ')
    