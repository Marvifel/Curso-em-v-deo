print('Progesiones Aritméticas (P.A.)')
print('=*=' *10)
pt = int(input('Escribe el primer término de una P.A.: '))   #se solicita al usuario escribir el primer término de la P.A.
r = int(input('Escribe la razón de esa P.A.: '))
termino = pt   #Se inicia la P.A. con el primer término
c = 1   #Se inicializa un contador en 1
total = 0   #Se inicializa otro contador en 0
mas = 10   #Por defecto, la progresión será de 10 términos, si el usuario no indica otra cantidad
while mas != 0:
    total = total + mas
    while c <= total:
        print(f'{termino} -> ', end='')
        termino = termino + r
        c += 1
    print('PAUSA')
    mas = int(input('¿Cuántos términos de más usted quiere ver?: '))
print('Progresión Aritmética finalizada con {} términos mostrados.'.format(total))
