# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def zipper(l1, l2):
    # Desconbrindo o menor indice entre as duas listas.
    intervalo_minimo = min(len(l1), len(l2))
    # Retornando uma listcomprehension com uma tupla.
    return [(l1[i], l2[i]) for i in range(intervalo_minimo)]

lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']

print(zipper(lista1, lista2))


# A função zip, faz a mesma coisa do codigo a cima.
print(list(zip(lista1, lista2)))

# O itertools faz o comtrario o zip, pega a lista maior
from itertools import zip_longest
# fillvalue é para quando um estiver faltando indice, um none, uma lista maior que outra
print(list(zip_longest(lista1, lista2, fillvalue='SEM CIDADE')))