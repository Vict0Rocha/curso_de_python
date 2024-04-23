from abc import ABC, abstractclassmethod

class Log(ABC):
    @abstractclassmethod # Dizendo que esse metodo é abstrato
    def _log(self, msg): #Assinatura da minha classe
        ...

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Seccess: {msg}')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


lp = LogPrintMixin()
lp.log_success('Estou aprendendo OO')
