nome = 'Victor'
print('V' in nome) #Para verificar se está entre alguma coisa
print(10 * '-')
print('V' not in nome) #Não está entre alguma coisa 
print(10 * '-')

nome = input('Digite seu nome <<< ')
palpite = input('Digite oque vc quer encontrar <<< ')

if palpite in nome:
    print(f'{palpite} está em {nome}')
else:
    print(f'{palpite} não está no {nome}')
