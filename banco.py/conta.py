from abc import ABC, abstractmethod

class Conta(ABC): #balance -> Saldo 
    def __init__(self, agencia, number, balance):
        self.agencia = agencia
        self.number = number
        self.balance = balance

    @abstractmethod
    def sacar(self, value: float) -> float: ...

    def depositar(self, value: float) -> float:
        self.balance += value
        print(f'DEPOSITO BEM SUCEDIDO - No valor de R${value}')
        self.detalhes()
        return self.balance

    def detalhes(self, msg: str = '') -> None:
        print(f'O seu saldo é R${self.balance:.2f} {msg}')

class ContaCorrente(Conta):
    def __init__(self, agencia, number, balance, limit: float):
        super().__init__(agencia, number, balance)
        self.limit = limit

    def sacar(self, value_saque: float) -> float:
        valor_pos_saque = self.balance - value_saque
        maximum_limit = -self.limit
        if valor_pos_saque >= maximum_limit:
            ...

class ContaPoupanca(Conta):
    def __init__(self, agencia, number, balance):
        super().__init__(agencia, number, balance)
    
    def sacar(self, value: float) -> float:
        ...

cc1 = ContaCorrente(111, 222, 0, 10)
cc1.depositar(10) 