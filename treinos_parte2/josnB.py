import json

CAMINHO_DO_ARQUVO = 'treinos_parte2\\dados.json'

class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome 
        self.idade = idade
        self.sexo = sexo
        
p1 = Pessoa('Victor', 19, 'Masculino')
p2 = Pessoa('Maria', 15, 'Feminino')
p3 = Pessoa('João', 20, 'Masculino')
bd = [vars(p1), p2.__dict__, vars(p3)]

with open(CAMINHO_DO_ARQUVO, 'w', encoding='utf-8') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)