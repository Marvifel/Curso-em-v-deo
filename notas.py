def notas(*n, sit=False):
    """
    ->Función para analizar notas y situaciones de varios alumnos.
    :param n: una o más notas de los alumnos (acepta varias).
    :param sit: valor opcional, indicando si debe o no agregar la situación.
    :return: diccionario con varias informaciones sobre la situación del grupo.
    """
    r = dict()
    r['total'] = len(n)
    r['mayor'] = max(n)
    r['menor'] = min(n)
    r['promedio'] = sum(n) / len(n)
    if sit:
        if r['promedio'] > 6.5:
            r['situación'] = 'Buena'
        elif 6.5 <= r['promedio'] < 5:
            r['situación'] = 'Razonable'
        else:
            r['situación'] = 'Mala'
    return r


#Programa Principal
resp = notas(3, 9, 1, 9.5, 2, sit=True)
print(resp)
