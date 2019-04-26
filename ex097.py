# Função
def titulo(msg):
    print('=' * (len(msg) + 2))
    print(f' {msg} ')
    print('=' * (len(msg) + 2))


# Programa
msg = str(input('Título da lista: '))
titulo(msg)
