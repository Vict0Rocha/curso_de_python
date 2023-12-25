'''
Generator function não funções que podem pausar.
Elas pausam e depois podem continuar dali.
'''

# def generator(n=0):
#     yield 1 # Ele PAUSA a função aqui, não quebra.
#     print('continuando') 
#     yield 2
#     print('Mais uma vez...')
#     yield 3
#     print('terminou')
#     return('Acabou') # Levanta uma exeçao para parar

# print(next(gen))
# print(next(gen))
# print(next(gen))
# for n in gen:
#     print(n)

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n > maximum:
            return
        
# Fazendo a mesma coisa que um range, mais podendo pausar no meio do caminho.

gen = generator()

for n in gen:
    print(n)