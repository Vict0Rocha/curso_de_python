# Banco tem contas e clientes (Agregação)
#     * Checar se a agência é daquele banco
#     * Checar se o cliente é daquele banco
#     * Checar se a conta é daquele banco
# Só será possível sacar se passar na autenticação do banco (descrita acima)
# Banco autentica por um método.

from conta import ContaCorrente, ContaPoupanca
from pessoa import Pessoa

class Banco:
    def __init__(self):
        ...

    def teste(self):
        print('Olá')

cc1 = ContaCorrente(111, 222, 5, 100)
p1 = Pessoa('Victor', 19)
brasil = Banco()
brasil.teste()
