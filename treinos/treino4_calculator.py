while True:
    n1 = input('Digite o PRIMEIRO valor <<< ')
    n2 = input('Digite o SEGUNDO valor <<< ')
    operador = input('Digite o OPERADOR (+-*/) <<< ')

    valores_validos = None #None quer dizer, vazio
    n1_float = 0
    n2_float = 0

    try:
        n1_float = float(n1)
        n2_float = float(n2)
        valores_validos = True

    except:
        valores_validos = None

    if valores_validos is None:
        print('Um ou mais OPERADORES estão INCORRETOS!')
        continue #Para voltar ao inicio do código      
    operadores_permitidos = '+-*/'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue     

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
     
    print('Segue abaixo o resultado, confira!')
    if operador == '+':
        print(n1_float + n2_float)
    elif operador == '-':
        print(n1_float - n2_float)
    elif operador == '*':
        print(n1_float * n2_float)
    elif operador == '/':
        print(n1_float / n2_float)
    else:
        print('Nunca deveria chegar aqui!')

    sair = input('Você deseja [S]air? <<< ').lower().startswith('s') # islower é para deixar tudo minusculo, startswhith é para verificar a primeira letra 
    if sair is True:
        break