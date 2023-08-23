"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.

"""

# n1 = input('Digite um número: ')

# try:
#     n1 = int(n1)
#     if n1%2 == 0:
#         print(f'O número {n1} é PAR')
#     else:
#         print(f'O número {n1} é IMPAR')
# except:
#     print('VALOR INVALIDO')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# horario = input('Digite o horario do seu relogio: ')

# try:
#     horario = float(horario)
#     if horario >= 0 and horario <= 11:
#         print('BOM DIA')
#     elif horario >= 12 and horario <= 17:
#         print('BOA TARDE')
#     elif horario >= 18 and horario <=23:
#         print('BOA NOITE')
#     else:
#         print('Horario invalido')
# except:
#     print('[ERRO], por favor, digite apenas números inteiros')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu nome <<< ')
tamanho_do_nome = len(nome)

if tamanho_do_nome >= 1:
    if tamanho_do_nome <= 4:
        print('CURTO')
    elif tamanho_do_nome >= 5 and tamanho_do_nome <=6:
        print('NORMAL')
    else:
        print('GRANDE')
else:
    print('Digite no minimo uma letra')
