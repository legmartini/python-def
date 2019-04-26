# Funções
def fatorial(num=1, show=0):
    """
    Calcula o fatorial de um número
    :param num: número a ser fatorado
    :param show: mostra ou não o cálculo de fatoração
    :return: retorna o valor final da fatoração
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
    if show == 1:
        for c in range(num, 0, -1):
            print(f'{c}', end=' ')
        print(f'\nFatorial = {f}')
    else:
        print(f'\nFatorial = {f}')


# Programa
num = int(input('Digite um número para saber seu fatorial: '))
show = int(input('Deseja ver o processo? 1-SIM 0-NÃO '))
fatorial(num, show)










