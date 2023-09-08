"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = '14382270006'
cpf_9_digito = cpf[:9] # Fazendo um fatiamento, pagando somente os 9 primeiros digitos
# cpf_9_digito = int(cpf_9_digito)

contagem = 10
resultado = 0

for digito in cpf_9_digito:
    resultado += int(digito)*contagem #Multiplicando digito por digito e já somando os resultos
    contagem = contagem - 1

resultado = (resultado * 10) % 11 #Multiplicando o resultado por 10 e pegando o resto da divisão por 11
print(resultado if resultado <= 9 else 0) # Caso o resultado seja maior que 9, o valor do primeiro digito deve valer 0