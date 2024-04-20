# Abstração
from pathlib import Path #Pacote que pega o caminho do meu arquivo

# Pegando o caminho do meu arquivo atual e concatenando um novo nome de arquivo
LOG_FILE = Path(__file__).parent / "log.txt"

class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Seccess: {msg}')

class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando no log:', msg_formatada)
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')
        
class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

if __name__ == '__main__':
    lp =  LogPrintMixin()
    lp.log_error('Minha mensagem')
    lp.log_success('Minha mensagem')
    lf = LogFileMixin()
    lf.log_error('Qualquer coisa')
    lf.log_success('Outra coisa')