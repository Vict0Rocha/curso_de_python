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
        print('-')

class ContaCorrente(Conta):
    def __init__(self, agencia, number, balance: float = 0, limit: float = 0):
        super().__init__(agencia, number, balance)
        self.limit = limit

    def sacar(self, value_saque: float) -> float:
        valor_pos_saque = self.balance - value_saque
        maximum_limit = -self.limit

        if valor_pos_saque >= maximum_limit:
            self.balance -= value_saque
            print(f'SAQUE BEM SUCEDIDO no valor de R${value_saque}')
            self.detalhes()
            return self.balance

        print('SAQUE NEGADO - Valor indisponivel para saque.')
        print(f'Seu limite é, {maximum_limit:.2f}')
        

class ContaPoupanca(Conta):
    def sacar(self, value_saque: float) -> float:
        if self.balance >= value_saque:
            self.balance -= value_saque
            print(f'SAQUE BEM SUCEDIDO no valor de R${value_saque}')
            self.detalhes()
            return self.balance
            
        print('SAQUE NEGADO - Valor indisponivel para saque.')
        self.detalhes()

if __name__ == '__main__':
    cp1 = ContaPoupanca(111, 222)
    cp1.sacar(1)
    cp1.depositar(1)
    cp1.sacar(1)
    cp1.sacar(1)
    print(30*'-')
    cc1 = ContaCorrente(111, 222, 0, 100)
    cc1.sacar(1)
    cc1.depositar(1)
    cc1.sacar(1)
    cc1.sacar(1)
    cc1.sacar(1)
    cc1.sacar(98)