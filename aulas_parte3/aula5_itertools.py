# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from itertools import combinations, permutations, product

def imprimir(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoa = ['Victor', 'Luana', 'Marcia', 'Juciley']
camiseta = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['marculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]

print('Combinação')
imprimir((combinations(pessoa, 2)))
print('Permutação')
imprimir(permutations(pessoa,2))
print('Produto')
imprimir(product(*camiseta))