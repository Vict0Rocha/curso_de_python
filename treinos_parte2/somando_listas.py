def soma(l1, l2):
    # if len(l1) <= len(l2):
    #     menor_lista =  len(l1)
    # else:
    #     menor_lista = len(l2)
    menor_lista = min(len(l1), len(l2))
    return [l1[i] + l2[i] for i in range(menor_lista)]
    
lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = [1, 2, 3, 4, 5]

print(soma(lista1, lista2))

# Aqui faz a mesma coisa 
soma_lista = [(x + y) for x, y in zip(lista1, lista2)]
print(soma_lista)
