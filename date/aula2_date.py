# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects

from datetime import datetime

fmt = '%d/%m/%Y %H:%M:%S'
data_fim = datetime.strptime('12/12/2022 08:20:20', fmt)
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)

print(data_fim - data_inicio)