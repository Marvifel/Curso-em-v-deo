#Este programa recrea el conocido juego de Piedra, Papel o Tijera
from random import randint
from time import sleep
print(f'{Piedra, Papel o Tijera:=^40}')
itens = ('Piedra', 'Papel', 'Tijera')   #Tupla que contiene las tres únicas opciones
print('''Elige una opción:
[0] Piedra
[1] Papel
[2] Tijera''')
elección = int(input('Tu elección: '))
print('\033[1;32mPiedra...\033[m')
sleep(1)
print('\033[1;35mPapel...\033[m')
sleep(1)
print('\033[1;34mTijera...\033[m')
pc = randint(0, 2)
print(f'La pc eligió {itens[pc]}.\nTú elegiste {itens[elección]}.')
if (elección == 0 and pc == 1) or (elección == 1 and pc == 2) or (elección == 2 and pc == 0):
    print('\033[1;34m¡PC gana!\033[m')
elif (pc == 0 and elección == 1) or (pc == 1 and elección == 2) or (pc == 2 and elección == 0):
    print('\033[1;36m¡JUGADOR gana!\033[m')
else:
    print('\033[1;32mEmpate!!!\033[m')
print('\033[7;30m¡Gracias por jugar!\033[m')
