def factorial(n, show=False):
    """
    ->Calcula el Factorial de un número.
    :parámetro n: Es el número que será calculado.
    :parámetro show: (opcional) Muestra o no el cálculo.
    :return: El valor del factorial de un número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


#Programa Principal
#print(factorial(5, show=True))
help(factorial)
