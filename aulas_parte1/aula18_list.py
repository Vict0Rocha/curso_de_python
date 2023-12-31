"""
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Luiz')
nome = lista.pop() #Removendo ultimo indice 
lista.append(1233) #Adicionando o ultimo indice
print(lista)
del lista[-5] #Deletando indice desejado
print(lista)
# lista.clear()
lista.insert(100, 5)
print(lista[4])

#Concatenando str

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy() #Para copiar uma lista