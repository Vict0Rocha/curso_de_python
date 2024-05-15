# json.dumps e json.loads com strings + typing.TypedDict
# Ao converter de Python para JSON:
# Python        JSON
# dict          object
# list, tuple   array
# str           string
# int, float    number
# True          true
# False         false
# None          null

import json
import pprint 
from typing import TypedDict

# Somente uma classe para tipar, não é obrigatória
class Movie(TypedDict):
  title: str
  original_title: str
  is_movie: bool
  imdb_rating: float
  year: int
  characters: list[str]
  budget: None | float

str_json = '''
{
  "title": "O Senhor dos Anéis: A Sociedade do Anel",
  "original_title": "The Lord of the Rings: The Fellowship of the Ring",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
  "budget": null
}
'''
# Carregando uma string que está em json, para a estrutura python
filme: Movie = json.loads(str_json)
pprint.pprint(filme)
print(filme['year'] + 3 )
# Sómente fazendo um print bonito
print(json.dumps(filme, ensure_ascii=False, indent=2))