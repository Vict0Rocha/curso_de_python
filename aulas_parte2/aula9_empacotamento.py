'''
Empacotamento de dicionarios
'''

pessoa = {
    'nome': 'Victor',
    'sobrenome': 'Cordeiro',
}

dados_pessoa = {
    'altura': 1.75,
    'pesso': 77,
}

# Juntando 2 dicionarios em 1.
pessoa_completa = {**pessoa, 'chave': 'valor', **dados_pessoa}
print(pessoa_completa)

# Passando a chave e valor para as variaveis atravez da função items.
(a1, a2), (b1, b2) = pessoa.items()

print(a1, a2)
print(b1, b2) 

# A função items nos permite acessar a chave e valor do dict
for chave, valor in pessoa.items():
    print(valor)

# kwargs - keyword arguments (argumentos nomeados)
    
def mostrar_args_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS: ', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

mostrar_args_nomeados('valor não nomeado', 9999, chave='valor', nome='Vitão', tell=123,)

mostrar_args_nomeados(**pessoa_completa)