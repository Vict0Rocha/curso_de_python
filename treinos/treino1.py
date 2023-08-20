nome = input('Digite o seu nome <<< ') 
idade = input('Digite a sua idade <<< ')

if nome and idade:
    idade = int(idade)
    print(f'Olá, {nome}!')
    print(f'Seu nome invertido é {nome [::-1]}')

    if ' ' in nome:
        print('Seu nome TEM espaço')
    else:
        print('Seu nome NÃO tem espaço')

    print(f'Seu nome tem {len(nome)} letra')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    
    print('Desculpe, você deixou campos vazios.')