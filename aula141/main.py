from log import LogFileMixin, LogPrintMixin
from eletronico import Smartphone

iphone = Smartphone('iPhone 14')
xiaomi = Smartphone('Redmi')

iphone.ligar()
iphone.desligar()