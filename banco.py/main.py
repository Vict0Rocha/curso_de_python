"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clintes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""

from abc import ABC, abstractmethod


class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome, idade):
        self._nome = nome 
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, new_nome):
        self._nome = new_nome
    
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, new_idade):
        self._idade = new_idade

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)


class Conta(ABC):
    @abstractmethod
    def __init__(self, agencia, numero_conta, saldo):
        self._agencia = agencia
        self._numero_conta = numero_conta
        self._saldo = saldo
    
    def depositar(self, valor_do_deposito):
        self._saldo += valor_do_deposito

    def sacar(self, valor_de_saque):
        if self._saldo >= valor_de_saque:
            self._saldo -= valor_de_saque
            print('Sucesso!')
        else:
            print('Você exedeu todo o seu saldo disponivel')
            raise ValueError

class ContaCorrete(Conta):
    def __init__(self, agencia, numero_conta, saldo):
        super().__init__(agencia, numero_conta, saldo)
        self._saldo_extra = 50

    def sacar(self, valor_de_saque):
        try:
            super().sacar(valor_de_saque)
        except ValueError:
            valor_disponivel_saque = self._saldo + self._saldo_extra

            if valor_disponivel_saque >= valor_de_saque:
                self._saldo_extra -= valor_de_saque
                print('Sucesso')
            else: 
                print('Saque NÃO ACEITO, valor indisponivel para saque.')

class ContaPoupanca(Conta):
    def __init__(self, agencia, numero_conta, saldo):
        super().__init__(agencia, numero_conta, saldo)

# class Banco:
#     def __init__(self, conta, cliente):
    

eu = Cliente('Victor', 19)
corrente = ContaCorrete('0805', 9964, 100)
poupanca = ContaPoupanca('0805', 9964, 100)
