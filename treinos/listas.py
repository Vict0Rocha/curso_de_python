import os

lista = []
condicao = True

while condicao == True:
    # print('-'*15)
    # print('FAÇA UMA LISTA')
    # print('-'*15)
    print('\nDigite oque deseja realizar')
    print('[A]adicionar [D]eletar [L]listar [S]sair')
    escolha = input(' ')

    if escolha == 'a':
        os.system('cls')
        item = input('Digite o item que deseja <<< ')
        lista.append(item)

    elif escolha == 'd':
        os.system('cls')
        indice_digitado = input('Digite o índice do ítem que deseja remover <<< ')
        
        try:
            indice_remover = int(indice_digitado)
            del lista[indice_remover]
        except ValueError:
            print('[ERRO] - Por favor, digite somente inteiros.')
        except IndexError:
            print('[ERRO] - Índice não existe na sua lista.')
        except Exception:
            print('[ERRO] - Problema não identificado pelo sistema.')

    elif escolha == 'l':
         os.system('cls')

         if len(lista) <= 0:
             print('Nada para lista! ')

         for i, item in enumerate(lista): #Para percorrer indice por indice de uma lista
             print(i, item)

    elif escolha == 's':
         break
    else:
        print('Digite somente: A, D, ou L')
        