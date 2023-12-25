
# ERROS.
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

# Try - Except - Else - Finally
# Finally sempre é executado
# Else é caso não de erro. (Um pouco de redundancia do finally).d
# Except para eceções.
try:
    print('Abrir o arquivo')
    8/0
except ZeroDivisionError as e: # Tratando o erro e atribuindo para uma variavel.
    print(e.__class__.__name__) # Exibindo o nome do erro, o mesmo de sua classe.
    print(e)
    print('Dividiu por 0')
except (IndexError, ImportError): # Tratando dois erros ao mesmo tempo.
    print('Mensagem')
else: # Caso o except não seja executado.
    print('Não deu erro')
finally: # Sempre sera executado.
    print('Fechar o arquivo')

# (Parte 2) try e except para tratar exceções
# a = 18
# b = 0
# c = a / b

# try:
#     a = 18
#     b = 0
#     # print(b[0])
#     # print('Linha 1'[1000])
#     c = a / b
#     print('Linha 2')
# except ZeroDivisionError as e: # Para atribuir um erro para uma variavel.
#     print(e.__class__.__name__) # Buscando o nome do erro.
#     print(e)
# except NameError:
#     print('Nome b não está definido')
# except (TypeError, IndexError) as error:
#     print('TypeError + IndexError')
#     print('MSG:', error)
#     print('Nome:', error.__class__.__name__)
# except Exception:
#     print('ERRO DESCONHECIDO.')

# print('CONTINUAR')
