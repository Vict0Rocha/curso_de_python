# Variáveis livres + nonlocal (locals, globals)]
'''
O nunlocal é para alterar o valor de variavel externas, dentro de outra 
função interna, o python por padrão permite acessar o valor, mas não 
realizar alternações na valor original da variavel.
'''

def fora(texto):
    variavel = texto
    def dentro(outro_texto):
        nonlocal variavel
        # concatenacao = variavel + outro_texto
        variavel += outro_texto
        return variavel 
    return dentro

text1 = fora('a')

print(text1('b'))

# Definição da documentação do python.

# A instrução nonlocal faz com que os identificadores listados se refiram a variáveis vinculadas 
# anteriormente no escopo mais próximo, excluindo globais. Isso é importante porque o comportamento 
# padrão para ligação é pesquisar primeiro o espaço de nomes local. A instrução permite que o código
# encapsulado ligue novamente variáveis fora do escopo local além do escopo global (módulo).

# Os nomes listados em uma instrução nonlocal, diferentemente daqueles listados em uma instrução global, 
# devem se referir a associações preexistentes em um escopo delimitador (o escopo no qual uma nova 
# associação deve ser criada não pode ser determinado inequivocamente).
