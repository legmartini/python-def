from random import randint


# Funções
def sorteio(lista):
    print('Sorteando 5 valores...')
    for cont in range(0, 5):
        n = randint(1, 101)
        lista.append(n)
        print(f'|{n}', end='| ')
    print('\nSorteio Finalizado. Boa Sorte!')


def soma(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos PARES é {soma}.')


# Programa
numeros = list()
sorteio(numeros)
soma(numeros)
