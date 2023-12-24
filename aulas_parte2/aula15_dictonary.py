# Dictionary Comprehension e Set Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

#Dict comprehension
dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave != 'categoria'
}

# Aqui tenho uma que parece um dict
lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('b', 'valor a'),
]

# Criando um dict a partir da minha lista
dc = {
    chave: valor
    for chave, valor in lista
}
print(dc)

# Set comprehension
s1 = {2 ** i for i in range(10)}
print(s1)