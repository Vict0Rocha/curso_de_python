# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sugar" (Açúcar sintático)

def is_string(string):
    if not isinstance(string, str):
        raise TypeError('O parametro deve ser uma string')

def cria_funcao(func):
    def interna(*args, **kwargs):
        print('Vou decorar minha function')
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O resultado é {resultado}')
        print('Function já decorada')
        return resultado
    return interna

@cria_funcao # Aqui é como se ele executasse a função chamada. 
# Esse funçaõ invert_string vira a função interna.
def invert_string(string):
    print(f'{invert_string.__name__}')
    return string[::-1]

# invert_string_checando = cria_funcao(invert_string)
# print(invert_string_checando('Victor'))

print(invert_string('TESTE'))