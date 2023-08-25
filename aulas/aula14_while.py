contador = 0

while contador <= 10:
    
    contador += 1

    if contador >= 4 and contador <= 5:
        print(f'Não vou mostra o {contador}')
        continue

    print(contador)

    if contador == 6:
        break