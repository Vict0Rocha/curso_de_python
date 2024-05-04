# Banco tem contas e clientes (Agregação)
#     * Checar se a agência é daquele banco
#     * Checar se o cliente é daquele banco
#     * Checar se a conta é daquele banco
# Só será possível sacar se passar na autenticação do banco (descrita acima)
# Banco autentica por um método.

import conta 
import pessoa

class Banco:
    def __init__(self,
            agencias: list[int] | None = None,
            clientes: list[pessoa.Pessoa] | None = None,
            contas: list[conta.Conta] | None = None
    ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []
 
    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            print('_checa_agencia', True)
            return True
        print('_checa_agencia', False)
        return False

    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            print('_checa_cliente', True)
            return True
        print('_checa_cliente', False)
        return False
        

    def _checa_conta(self, conta):
        if conta in self.contas:
            print('_checa_conta', True)
            return True
        print('_checa_conta', False)
        return False
    
    def _checa_se_conta_e_do_cliente(self, cliente, conta):
        if conta is cliente.conta:
            print('_checa_se_conta_e_do_cliente', True)
            return True
        print('_checa_se_conta_e_do_cliente', False)
        return False
        
    def autenticar(self, cliente: pessoa.Pessoa, conta:conta.Conta):
        return self._checa_agencia(conta) and \
        self._checa_cliente(cliente) and \
        self._checa_conta(conta) and \
        self._checa_se_conta_e_do_cliente(cliente, conta) 
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name} {attrs}'

if __name__ == '__main__':
    luiz = pessoa.Cliente('Luiz', 30)
    cc1 = conta.ContaCorrente(111, 222, 0, 100)
    luiz.conta = cc1

    maria = pessoa.Cliente('Maria', 18)
    cc2= conta.ContaPoupanca(222, 223, 100)
    maria.conta = cc2
    banco = Banco()
    # print(banco) 

    banco.clientes.extend([maria, luiz])
    banco.contas.extend([cc1, cc2])
    banco.agencias.extend([111, 222, 333])
    # print(banco.autenticar(luiz, cc1))
    # print(banco) 

    if banco.autenticar(luiz, cc1):
        luiz.conta.depositar(100)
        luiz.conta.sacar(190)