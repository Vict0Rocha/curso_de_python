# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime
from dateutil.relativedelta import relativedelta

# A linguagem permite o " _ " só para facilitar a leitura
valor_total = 1_000_000 
data_emprestimo = datetime(2020, 12, 20) # Pegando a data de inicio
delta_anos = relativedelta(years=5) #Pegando 5 anos
data_final = data_emprestimo + delta_anos 
'''
Enquanto a data da minha parcela não chegar no final do financiamento,
vou adicionar mais um mês e colocar a data na minha lista de datas.
'''
data_parcelas = []
data_parcela = data_emprestimo
while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

# Pegando a quantidade de datas
numero_parcelas = len(data_parcelas)
valor_parcela = valor_total / numero_parcelas

for data in data_parcelas:
    print(data.strftime('%d/%m/%Y'), f'R${valor_parcela:.2f}')
