palavra_secreta = 'python'

print('-'*27)
print('ADIVINHE A PALAVRA SEGRATA')
print('-'*27)
 
palpite = ' '
tentativas = 0

while palpite != palavra_secreta:
    palpite = input('Digite seu palpite <<< ')

    if len(palpite) > 1:
        print('[ERROS] - palpite não salvo')
        print('Digite apenas uma letra!')
        continue

    palpite = palpite.upper()
    print(palpite)
    # for i in palavra_secreta:
    #     if palpite == i:
    #         print('ok')
    print('Errou')

