from time import sleep

c = ('\033[m',
     '\033[0;30;41m',
     '\033[0;30;42m',
     '\033[0;30;43m',
     '\033[0;30;44m',
     '\033[0;30;45m',
     '\033[7;30m',
     )


# Funções
def ajuda(cmd):
    titulo(f'  Acessando o manual do comando  \'{cmd}\'', 4)
    print(c[6], end='')
    help(cmd)
    print(c[0], end='')
    sleep(1.5)


def titulo(msg, cor):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('=' * tam)
    print(f'  {msg}')
    print('=' * tam)
    print(c[0], end='')


# Programa
comando = ''
while True:
    titulo('Sistema de Ajuda PYHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até Logo!', 1)
