cpf = '74682489070'
cpf_9_digito = cpf[:9] # Fazendo um fatiamento, pagando somente os 9 primeiros digitos
contagem_1 = 10
resultado_1 = 0

for digito in cpf_9_digito:
    resultado_1 += int(digito) * contagem_1 # Multiplicando digito por digito e já somando os resultos
    contagem_1 -= 1

resultado_1 = (resultado_1 * 10) % 11 # Multiplicando o resultado por 10 e pegando o resto da divisão por 11
resultado_digito_1 = resultado_1 if resultado_1 <= 9 else 0 # Caso o resultado seja maior que 9, o valor do primeiro digito deve valer 0
print(resultado_digito_1) 

cpf_10_digito = cpf[:10]
contagem_2 = 11
resultado_2 = 0

for digito in cpf_10_digito:
    resultado_2 += int(digito) * contagem_2
    contagem_2 -= 1

resultado_2 = resultado_2 * 10 % 11
resuldado_digito_2 = resultado_2 if resultado_2 <= 9 else 0
print(resuldado_digito_2)