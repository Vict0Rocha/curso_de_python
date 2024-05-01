'''Pessoa
Recebe dois valores.
name: str
idade: int
'''
class Pessoa: #age =  idade
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
         self._name = new_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        self._age = new_age

p = Pessoa('Victor', 18)
