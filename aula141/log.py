# Abstração

class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Seccess: {msg}')

class LogFileMixin(Log):
    def _log(self, msg):
        print(msg)
        
class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

if __name__ == '__main__':
    l =  LogPrintMixin()
    l.log_error('Minha mensagem')
    l.log_success('Minha mensagem')