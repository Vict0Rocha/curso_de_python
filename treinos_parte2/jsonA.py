import json
from josnB import Pessoa, CAMINHO_DO_ARQUVO

with open(CAMINHO_DO_ARQUVO, 'r', encoding='utf-8') as arquivo:
    pessoas = json.load(arquivo)
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])

print(vars(p1))
print(vars(p2))
print(vars(p3))