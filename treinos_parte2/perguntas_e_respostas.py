
# Criando um lista que recebe varios dicionarios
perguntas_e_repostas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '4', '3', '8'],
        'Resposta': '4',    
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '30', '20'],
        'Resposta': '25',    
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['10', '5', '2', '8'],
        'Resposta': '5',    
    },
]

qtd_acertos = 0
for pergunta in perguntas_e_repostas: #Percorrendo toda a lista de pergunta e respostas
    print('Pergunta:', pergunta['Pergunta']) # Escrevendo o valor de cada pergunta
    print()
    
    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i}) {opcao}')
    print()

    escolha = input('Escolha uma opção: ')
    escolha_int = None
    acerto = False
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)
    
    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acerto = True
    
    print()
    if acerto:
        qtd_acertos += 1
        print('Acertou ✅ ')
    else:
        print('Errou ❌ ')

print(f'Você acertou {qtd_acertos} de {len(pergunta)} perguntas!')