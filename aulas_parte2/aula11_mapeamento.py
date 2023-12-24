lista = [numero * 2 for numero in range(10)]

# print(lista)

# Mapeamento de dados um list comprehension
produtos = [
    {'nome': 'p1', 'valor': 20},
    {'nome': 'p2', 'valor': 10},
    {'nome': 'p3', 'valor': 30},
]

# Mapeando para uma nova lista os dados.
novo_produtos = [produto['valor'] for produto in produtos]

# Criando um novo dict e aumentando os valores do produto em 5%
novo_produtos = [{**produto, 'valor': produto['valor'] * 1.05} for produto in produtos]

# Criando um novo dict e aumentando os valores dos produtos que sejam maior que 20
novo_produtos = [{**produto, 'valor': produto['valor'] * 1.05}
                 if produto['valor'] > 20 else {**produto}
                 for produto in produtos
]

# Desempacotando e separando por quebra de linha
print(*novo_produtos, sep='\n')
