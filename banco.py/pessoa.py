'''Pessoa
Recebe dois valores.
name: str
idade: int
'''
class Pessoa: #age =  idade
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
         self._name = new_name

p = Pessoa('Victor', 18)
print(p.name)
p.name = 'João'
print(p.name)