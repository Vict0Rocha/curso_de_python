# Modulo de print 
import pprint

# Uma simples função com a config do print que queremos 
def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

produtos = [
    {'nome': 'p1', 'valor': 20},
    {'nome': 'p2', 'valor': 10},
    {'nome': 'p3', 'valor': 30},
]

novos_produtos = [
    {**produto, 'valor': produto['valor'] * 1.05}
    if produto['valor'] > 20 else {**produto}
    for produto in produtos if produto['valor'] > 10
]

p(novos_produtos)