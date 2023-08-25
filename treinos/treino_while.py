"""
Iterando strings com while
"""
#       012345678910
# nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321


# nome = 'Maria Helena'  # Iteráveis

# indice = 0
# novo_nome = ''
# while indice < len(nome):
#     letra = nome[indice]
#     novo_nome += f'*{letra}'
#     indice += 1

# novo_nome += '*'
# print(novo_nome)

nome = 'Victor Hugo'
tamanho_nome = len(nome)
nova_str = ''
contador = 0

while contador < tamanho_nome:
    nova_str = nome[contador]
    print(nova_str, end='*')
    contador += 1

