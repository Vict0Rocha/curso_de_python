import conta

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

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.name!r}, {self.age!r})'
        return f'{class_name} {attrs}'
    
class Cliente(Pessoa):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.conta: conta.Conta | None = None

if __name__ == '__main__':
    c1 = Cliente('Luiz', 30)
    c1.conta = conta.ContaCorrente(111, 222, 0, 0)
    print(c1)
    print(c1.conta)
    c2 = Cliente('Maria', 18)
    c2.conta = conta.ContaPoupanca(112, 223, 100)
    print(c2)
    print(c2.conta)