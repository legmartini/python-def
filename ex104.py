# Funções
def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO!')
        if ok:
            break
    return valor


# Programa
n = leiaint('Digite um número: ')
print(f'Você acabou de inserir o número {n}.')

