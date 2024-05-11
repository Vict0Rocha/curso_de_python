# locale para internacionalização (tradução)
# https://docs.python.org/3/library/locale.html
# https://learn.microsoft.com/fr-fr/powershell/module/international/get-
# winsystemlocale?view=windowsserver2022-ps&viewFallbackFrom=win10-ps
import calendar
import locale
'''Comando para ver os locais deponives do sistema
digitar no terminal - Get-WinSystemLocale
'''

# Usando a localização padrão do sistema operacional
locale.setlocale(locale.LC_ALL, '')
# print(locale.getlocale())
print(calendar.calendar(2024))