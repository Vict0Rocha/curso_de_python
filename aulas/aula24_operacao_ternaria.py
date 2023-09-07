'''
Operação ternária (condicional de uma linha)
<valor> if <condição> else <outro valor>
'''

# condicao = 10 == 10 #Condição está valendo True
# varialvel = 'Verdadeiro' if condicao else 'Falso'
# print(varialvel)

digito = 2
# novo_digito = digito if digito <= 9 else 0
novo_digito = 0  if digito > 9 else digito
print(novo_digito)