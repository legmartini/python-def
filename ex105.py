# Funções
def notas(*n, sit=False):
    """
    Programa para mostrar os dados de notas de algum aluno.
    :param n: Notas do aluno
    :param sit: Mostra a situação do aluno. (aprovado ou reprovado)
    :return: retorna o dicionário com as informações
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n)/len(n)

    if sit:
        if r['Média'] < 7:
            r['Situação'] = 'Reprovado'
        elif r['Média'] >= 7:
            r['Situação'] = 'Aprovado'

    return r


# Programa
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)


