# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).

import os
from itertools import count # Count é um contador 

caminho = os.path.join('\\Users', 'victo', 'OneDrive','Imagens',
'Capturas de tela')
# Instanciando meu contador  
counter = count()

#  Percorrendo todas as pastas do meu caminho passado
for root, dirs, files in os.walk(caminho):
    # Pegando o proximo elemento do meu contador 
    the_counter = next(counter)
    print(the_counter,'Pasta atual', root)

    # Percorrendo todos os diretórios 
    for dir_ in dirs:
        print(' ', the_counter, 'Diretório atual', dir_)

    # Percorrendo todos os meus arquivos 
    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        # Pegando o caminho completo do meu arquivo
        print(' ', the_counter, 'File', caminho_completo_arquivo, files)
        # NÃO FAÇA ISSO (VAI APAGAR TUDO DAS PASTAS)
        # os.unlink(caminho_completo_arquivo)