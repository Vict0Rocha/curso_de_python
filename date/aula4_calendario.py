# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo

import calendar

# print(calendar.calendar(2024)) # Imprimi o calendario na tela
# print(calendar.month(2024, 5))

# O valor a esquerda representa o nome(em número) do primeiro dia do mês
# A direita o ultimo dia do mês.
print(calendar.monthrange(2024, 5))
numero_primeiro_dia, numero_ultimo_dia =  calendar.monthrange(2022, 12)
# Mostrao o valor e o nome de cada dia da semana
# print(list(enumerate(calendar.day_name)))
print(calendar.day_name[numero_primeiro_dia])
# Número do dia da semmana do ultimo dia do mês
print(calendar.weekday(2024, 5, numero_ultimo_dia)) 
print(calendar.day_name[calendar.weekday(2024, 5, numero_ultimo_dia)]) 

# Retorna os dias das semanas, onde marcar "0", é pq o dia não é do mês
# print(calendar.monthcalendar(2024, 5))
for week in calendar.monthcalendar(2024, 5):
    print(week)