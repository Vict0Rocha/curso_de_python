# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

import copy

# Lista de dicionarios
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Função para percorrer as lista
def imprimir(lista):
    for item in lista:
        print(item)

# Criando uma nova variavel - Desempacotando e passando os dados para filtro a esquerda do for.
#Percorrendo e fazendo uma copia profunda da lista original.
novos_produtos =[
    {**produtos, 'preco': round(produtos['preco'] * 1.1, 2)} 
    for produtos in copy.deepcopy(produtos)
]

# Usando sorted para ordenar minha lista, passando a função lambda como parametro
# Reverse é para ordenar de forma crescente ou decrescente.
produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos), 
    key=lambda item: item['nome'], reverse=True
)

# produtos_ordenados_por_preco = copy.deepcopy(sorted(produtos, key=lambda item: item['preco']))
produtos_ordenados_por_preco = sorted(copy.deepcopy(produtos), key=lambda item: item['preco'])

imprimir(produtos)
print()
imprimir(novos_produtos)
print()
imprimir(produtos_ordenados_por_nome)
print()
imprimir(produtos_ordenados_por_preco)