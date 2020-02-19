def leaInt(msj):
    while True:
        try:
            n = int(input(msj))
        except (ValueError, TypeError):
            print('\033[31m¡ERROR! Escribe un número entero válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mEl usuario prefirió no escribir el número.\033[m')
            return 0
        else:
            return n

def leaFloat(msj):
    while True:
        try:
            n = float(input(msj))
        except (ValueError, TypeError):
            print('\033[31m¡ERROR! Escribe un número real válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31mEl usuario prefirió no escribir ese número\033[m')
            return 0
        else:
            return n








n1 = leaInt('Escribe un número entero: ')
n2 = leaFloat('Escribe un número real: ')
print(f'Los números escritos fueron {n1} y {n2}')
