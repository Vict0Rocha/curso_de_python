from datetime import datetime

fmt = '%d/%m/%Y'
data = datetime.strptime('2024-05-09 21:05:30', '%Y-%m-%d %H:%M:%S')
# print(data)  
print(data.strftime(fmt))  
print(data.strftime('%Y'))  
# De um lado a data em string e do outro a data em inteiro
print(data.strftime('%m'), data.month) 
print(data.strftime('%S'), data.second)  