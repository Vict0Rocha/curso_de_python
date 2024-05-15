import os
import json

NOME_ARQUIVO = 'aula10.json'

# Pegando o caminho absoluto do meu arquivo, "caminho partindo da raiz C:"
# abspath para pegar desda raiz
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(
    os.path.join(
        # Pegando o nome do diretório do meu arquivo 
        os.path.dirname(__file__),
        NOME_ARQUIVO
    )
)

filme = {
    'title': 'O Senhor dos Anéis: A Sociedade do Anel',
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring',
    
    'is_movie': True,
    'imdb_rating': 8.8,
    'year': 2001,
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],
    'budget': None
}

# Escrevendo no arquivo meu json
with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w') as arquivo:
    json.dump(filme, arquivo, ensure_ascii=False, indent=2)

# Lendo do arquvio meu json
with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r') as arquivo:
    filme_do_json = json.load(arquivo)
    print(filme_do_json)
