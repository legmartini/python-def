from time import sleep


# Funções
def linha():
    print('-=' * 20)


def contador(ini, fim, pas):
    print('-=' * 20)
    print(f'Contagem de {ini} até {fim} de {pas} em {pas}')
    sleep(1.5)

    if pas < 0:
        pas *= -1
    if pas == 0:
        pas = 1

    if ini < fim:
        cont = ini
        while cont <= fim:
            print(f'{cont} ', end='')
            cont += pas
            sleep(0.3)
        print('Fim!')
        sleep(0.7)

    if ini > fim:
        cont = ini
        while cont >= fim:
            print(f'{cont} ', end='')
            cont -= pas
            sleep(0.3)
        print('Fim!')
        sleep(0.5)


# Programa
contador(1, 10, 1)
contador(10, 0, 2)
linha()
ini = int(input('Início: '))
fim = int(input('Final: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
linha()



