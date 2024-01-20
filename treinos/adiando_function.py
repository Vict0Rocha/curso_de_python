# def cria_funcao(saudacao):
#     def saudar(pessoa):
#         return f'{saudacao}, {pessoa}'
#     return saudar

# falar_bom_dia = cria_funcao('Bom dia')
# falar_boa_noite = cria_funcao('Bom noite')

# print(falar_bom_dia('Luana'))

# nomes = ['Victor', 'Hugo', 'João']

# for nome in nomes:
#     print(falar_bom_dia(nome))
#     # print()
#     print(falar_boa_noite(nome))

'''
É como seu o codigo pausase no execução da segunda função.
Recebo uma função e um parametro, o python guardas esses dados,
não executa a função interna, ele fica esperando o fechamento,
quando é feito o fechamento, o python executa a função interna,
sendo possivel utilizar os dados passados para a função externa. 
'''

def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

def criar_funcao(funcao, x):
    def interna(y): # Fica aguardando o fechamento
        return funcao(x, y)
    return interna

# Nesse momento a função interna não é executada, ela fica esperando ser fechada,
# o python guarda os dados passados, e pode ser usado na função interna.
soma_com_cinco = criar_funcao(soma, 5) 
multiplica_por_dez = criar_funcao(multiplica, 10)

# Aqui é feito o fechamento e é passado o ultimo parametno
print(soma_com_cinco(5))  
print(multiplica_por_dez(5))