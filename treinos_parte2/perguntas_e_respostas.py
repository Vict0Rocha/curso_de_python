
# Criando um lista que recebe varios dicionarios
perguntas_e_repostas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '2', '3', '4'],
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

for pergunta in perguntas_e_repostas: #Percorrendo toda a lista de pergunta e respostas
    print('Pergunta: ', pergunta['Pergunta']) # Escrevendo o valor de cada pergunta
    # print('Opções: ', pergunta['Opções'])
    
    opcoes = pergunta['Opções']
    for i, opcoes in enumerate(opcoes):
        print(f'{i}) {opcoes}')
    print('')
