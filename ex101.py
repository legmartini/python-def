from datetime import date


# Funções
def voto(nasc):
    idade = date.today().year - nasc

    if idade < 16:
        print(f'Você tem {idade} anos e NÃO tem o direito de votar.')
    elif idade == 16 or idade == 17 or idade > 60:
        print(f'Você tem {idade} anos e seu voto é OPCIONAL.')
    elif idade >= 18 or idade <= 60:
        print(f'Você tem {idade} anos e seu voto é OBRIGATÓRIO.')


# Programa
nasc = int(input('Ano de nascimento: '))
voto(nasc)



