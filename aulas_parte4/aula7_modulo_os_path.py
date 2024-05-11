# os.listdir para navegar em caminhos

import os

'''Manipulando pastas e arquivos 
Aqui estou pegando um caminho de arquivo do meu S.O.
Abrindo todas as pastas desse caminho, e listando 
todos os arquivos dentros das pastas do meu camminho.
'''

# caminho = 'C:\Users\victo\OneDrive\Imagens\Capturas de tela'
# Pegando o caminho do meu arquivo
caminho = os.path.join('\\Users', 'victo', 'OneDrive','Imagens',
'Capturas de tela')

# Percorrendo as pastas nesses caminho
for pasta in os.listdir(caminho):
    # Montando o caminho completo do (caminho + pasta)
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)
    # Quando encontrar algo que não seja uma pasta, continue
    if not os.path.isdir(caminho_completo_pasta):
        continue
    
    # Quando entrar dentro da pasta, mostre todos os arquivos ai dentro
    for imagem in os.listdir(caminho_completo_pasta):
        print('  ', imagem)
