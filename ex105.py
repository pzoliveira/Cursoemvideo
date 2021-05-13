def notas(*ntprvs, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param ntprvs: Uma ou mais notas dos alunos (aceita várias).
    :param sit: Valor opcional, indica a adição da situação no retorno.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    aval = dict()
    aval['total'] = len(ntprvs)
    aval['maior'] = max(ntprvs)
    aval['menor'] = min(ntprvs)
    média = aval['média'] = sum(ntprvs)/len(ntprvs)
    if sit:
        if média < 5:
            aval['situação'] = 'RUIM'
        elif média < 7:
            aval['situação'] = 'RAZOÁVEL'
        elif média <= 10:
            aval['situação'] = 'BOA'
    return aval


# Programa Principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
print()
help(notas)
