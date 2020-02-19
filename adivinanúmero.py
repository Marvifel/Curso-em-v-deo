#La computadora va a"pensar" un número y el usuario debe adivinar
from random import choice
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pc = choice(lista)   #Este es el número que "pensó" la pc
acierto = False
intentos = 0
print('\033[1;37mLa PC ya pensó un número entre 1 y 10. Te reto a que adivines...\033[m')
while not acierto:
    jugador = int(input('Intenta adivinar: '))
    intentos += 1
    if jugador < pc:
        print('Intenta un número más alto')
    elif pc == jugador:
        acierto = True
    else:
        print('Intenta un número más bajo')
print(f'Acertaste, con {intentos} intentos. La pc pensó en el número {pc} ¡Felicitaciones!')
