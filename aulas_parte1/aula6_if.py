entrada = input("Vc quer [E]ntar ou [S]air \n")

if entrada == 'E' or 'e':
    senha = input('Digite a sua senha: ') or 'Sem senha'
    if senha == 123:
        print('Senha CORRETA')
    else:
        print('Senha incorrete')
else:
    print('Fim')

