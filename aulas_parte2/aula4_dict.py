pessoa = {} # Criando um dicionario

chave = 'nome'

pessoa[chave] = 'Vitor'
pessoa['sobrenome'] = 'Cordeiro'

print(pessoa)

pessoa[chave] = 'Vitão'

print(pessoa)

del pessoa['sobrenome']
print(pessoa)

if pessoa.get('sobrenome') is None:
    print('Valor não existe')
else:
    print(pessoa['sobrenome'])