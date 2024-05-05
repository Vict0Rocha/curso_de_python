# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
from datetime import datetime
from pytz import timezone

# data_str_data = '2024/05/05 07:49:23'
# data_str_data = '2024/05/05'
# data_str_fmt = '%Y/%m/%d'

# data = datetime(2024, 5, 5, 13, 5, 23)
# data = datetime.strptime(data_str_data, data_str_fmt)

# data = datetime.now(timezone('America/Cuiaba'))
data = datetime.now()

print(data.timestamp()) # Pegando meu timezone 
print(datetime.fromtimestamp(1714930437.986032)) # Exibindo meu timezone em data.