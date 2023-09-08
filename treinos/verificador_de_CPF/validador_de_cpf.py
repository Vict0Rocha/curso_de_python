import re
import sys

# cpf_usuario = '74682489070'
entrada_cpf = input('Digite o CPF: ')
cpf_usuario = re.sub(
    r'[^0-9]', # Pagando tudo que não é número 
    '', # Substituindo por nada 
    entrada_cpf # Passando o valor
)

entrada_sequencial = entrada_cpf == entrada_cpf[0] * len(entrada_cpf)

if entrada_sequencial:
    print('[ERRO] Você digitou somente itens repetidos!')
    sys.exit()

cpf_9_digito = cpf_usuario[:9] # Fazendo um fatiamento, pagando somente os 9 primeiros digitos
contagem_1 = 10
resultado_1 = 0

for digito in cpf_9_digito:
    resultado_1 += int(digito) * contagem_1 # Multiplicando digito por digito e já somando os resultos
    contagem_1 -= 1

resultado_1 = (resultado_1 * 10) % 11 # Multiplicando o resultado por 10 e pegando o resto da divisão por 11
digito_1 = resultado_1 if resultado_1 <= 9 else 0 # Caso o resultado seja maior que 9, o valor do primeiro digito deve valer 0
# print(digito_1)

cpf_10_digito = cpf_usuario[:10]
contagem_2 = 11
resultado_2 = 0

for digito in cpf_10_digito:
    resultado_2 += int(digito) * contagem_2
    contagem_2 -= 1

resultado_2 = resultado_2 * 10 % 11
digito_2 = resultado_2 if resultado_2 <= 9 else 0
# print(digito_2)

cpf_sistema = f'{cpf_9_digito}{digito_1}{digito_2}'
# print(cpf_sistema)
print(cpf_sistema)

if cpf_usuario == cpf_sistema:
    print(f'O {cpf_usuario} é VALIDO')
else:
    print(f'O {cpf_usuario} é INVÁLIDO')