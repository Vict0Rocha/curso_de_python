from abc import ABC, abstractmethod

class Conta(ABC): #balance -> Saldo 
    def __init__(self, agencia, number, balance = 0):
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

    def detalhes(self) -> None:
        print(f'O seu saldo é R${self.balance:.2f}')

class ContaCorrente(Conta):
    def __init__(self, agencia, number, balance, limit: float):
        super().__init__(agencia, number, balance)
        self.limit = limit

    def sacar(self, value_saque: float) -> float:
        valor_pos_saque = self.balance - value_saque
        maximum_limit = -self.limit
        if valor_pos_saque >= maximum_limit:
            self.balance -= value_saque
            print(f'Saque bem sucedido no valor de R${value_saque}')
            self.detalhes()
            return self.balance
        print('SAQUE NEGADO - Valor indisponivel para saque.')
        self.detalhes()
        

class ContaPoupanca(Conta):
    def __init__(self, agencia, number, balance):
        super().__init__(agencia, number, balance)
    
    def sacar(self, value_saque: float) -> float:
        if self.balance >= value_saque:
            self.balance -= value_saque
            print(f'SAQUE BEM SUCEDIDO no valor de R${value_saque}')
            self.detalhes()
            return self.balance
            
        print('SAQUE NEGADO - Valor indisponivel para saque.')
        self.detalhes()
