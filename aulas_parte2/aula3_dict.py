# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')


grade_do_curso = {
    'materia': 'Programação',
    'carga_horia': '180',   
    'sala': '12',
    'alunos': [
        {'nome': 'Victor', 'idade': 18},
        {'nome': 'João', 'idade': 20},
    ],
}
# grade_do_curso = dict(mateira='Banco de dados')
print(grade_do_curso['materia'])
print(grade_do_curso['carga_horia'])
print()

for chave in grade_do_curso:
    print(chave, grade_do_curso[chave])