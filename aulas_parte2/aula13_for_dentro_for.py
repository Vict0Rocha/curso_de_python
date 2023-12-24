lista = []

for x in range(3):
    for y in range(3):
        lista.append((x, y)) #Adicionando uma tupla em cada indice da minha lista
# Porque não é possivel adicinar dois valores em um unico indice.

# Oque fica do lado esquerdo do for. É oque sera incluido na lista nova.

lista = [
    (x, y) 
    for x in range(3)
    for y in range(3)
]

# Aqui tem uma list comprehension dentro de outra list comprehension
lista = [
    [letra for letra in 'Victor']
    for x in range(3)
]


print(lista)