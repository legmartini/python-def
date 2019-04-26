# Funções
def linha():
    print('-' * 30)


def maior(* num):
    cont = maior = 0
    print('Analisando os valores...')

    for valor in num:
        print(f'{valor}', end=' ')

        if cont == 0:
            maior = valor
        elif valor > maior:
            maior = valor
        cont += 1

    print(f'\nForam informados {cont} valores')

    print(f'O maior valor informado foi {maior}.')


# Programa
linha()
maior(2, 9, 4, 5, 7, 1)
linha()
maior(4, 7, 0)
linha()
maior(1, 2)
linha()
maior(6)
linha()
maior()
linha()
