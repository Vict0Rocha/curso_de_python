# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def criar_multiplicador(multiplicador):
    def multiplicar(valor):
        return valor * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicador = criar_multiplicador(3)
quadruplicador = criar_multiplicador(4)

valor = 2

print(duplicar(valor))
print(triplicador(valor))
print(quadruplicador(valor))
