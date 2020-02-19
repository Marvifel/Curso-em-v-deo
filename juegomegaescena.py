from time import sleep
from random import randint
lista = []
juegos = []
print('-' * 40)
print('     Juega en la Mega Escena     ')
print('-' * 40)
cant = int(input('¿Cuántos juegos quieres que sortee?: '))
total = 1
print('-=' * 3, f'\033[1mSORTEANDO {cant} JUEGOS\033[m', '-=' * 3)
while total <= cant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    juegos.append(lista[:])
    lista.clear()
    total += 1
for i,l in enumerate(juegos):
    print(f'Juego {i+1}: {l}')
    sleep(1)
print('-=' *5, 'BUENA SUERTE', '-=' *5)
