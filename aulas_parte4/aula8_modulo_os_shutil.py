# os + shutil - Apagando, copiando, movendo e renomeando pastas com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
# Copiar Árvore recursivamente -> shutil.copytree
# Apagar Árvore recursivamente -> shutil.rmtree
# Apagar arquivos -> os.unlink
# Renomear/Mover -> shutil.move ou os.rename

import os
import shutil

# Aqui esse modulo pega o home do meu usuario 
HOME = os.path.expanduser('~')
DOCUMENTOS = os.path.join(HOME, 'OneDrive', 'Documentos')
PASTA_ORIGINAL = os.path.join(DOCUMENTOS, 'EXEMPLO')
NOVA_PASTA = os.path.join(DOCUMENTOS, 'NOVA_PASTA')

# Excluindo uma pasta
shutil.rmtree(NOVA_PASTA)
# Faz a mesma coisa do codigo a baixo
# Copia os arquivos de uma pasta para outra
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)


# # Criando uma nova pasta, caso já exista, ok. ksks
# # os.makedirs(NOVA_PASTA, exist_ok=True)

# for root, dirs, files in os.walk(PASTA_ORIGINAL):
#     for dir_ in dirs:
#         caminho_novo_diretorio = os.path.join(
#             root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
#         )
#         # Criando as novas pastas que estamos copiando
#         os.makedirs(caminho_novo_diretorio, exist_ok=True)

#     for file in files:
#         caminho_arquivo = os.path.join(root, file)
#         # Trocando o caminho da pasta original para nova pasta no root
#         caminho_novo_arquivo = os.path.join(
#             root.replace(PASTA_ORIGINAL, NOVA_PASTA), file
#         )

#         shutil.copy(caminho_arquivo, caminho_novo_arquivo)