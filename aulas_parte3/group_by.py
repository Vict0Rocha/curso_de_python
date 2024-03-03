from itertools import groupby

# Uma lista de dicionarios, cada dicionario com nome e nota.
alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]
'''
Agrupando uma lista de dicionarios, por uma chave
'''

# Retorna a chave pela qual os alunos devem ser ordenados.
def ordena(alunos):
    return alunos['nota']

# Ordena a lista de alunos com base na chave 'nota'.
alunos_agrupados = sorted(alunos, key=lambda a: a['nota'])

# agrupar os alunos ordenados. O parâmetro key especifica uma 
# função que será aplicada a cada elemento antes de agrupá-los.
grupos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)