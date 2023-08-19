nome = 'Victor Hugo'
altura = 1.75
peso = 76
imc = peso / (altura*altura)

# print(nome, 'tem', altura, 'tem o peso de', peso, 'Kg')
# print('Seu IMC é: ', imc)

# f-string
linha_1 = f' Olá, {nome}, vc tem {altura:.2f} de altura e pesa {peso}Kg'
linha_2 = f'Seu IMC é {imc:.2f}'

print(linha_1)
print(linha_2)
