import os

palavra_secreta = 'python'
palpite = ''
tentativas = 0
jogo =True
letra_certa = ''
palavra_formada = ''

while jogo == True:
    print('Adivinhe a palavra secreta')
    
    # for letra_palpite in palavra_secreta:
    #     print(end = (' _ '))
    palpite = input('Digite uma letra: ')
    
    tentativas += 1
    
    if len(palpite) > 1:
        print('Digite apenas uma letra')
        continue
    
    if palpite in palavra_secreta:
       letra_certa += palpite
       
    palavra_formada = ''
    for letra_palpite in palavra_secreta:
        if letra_palpite in letra_certa:
           palavra_formada += letra_palpite
        else:
             palavra_formada += '*'
        
    print(palavra_formada)
    
    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('Parabéns, VOCÊ GANHOU!')
        print('A palavra segreta era', palavra_secreta)
        print('Total de tentativas:', tentativas)
        tentativas = 0
        letra_certa = ''
