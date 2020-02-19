from random import randint
print('=*=' * 30)
print((' ' * 10),'\033[1m*Vamos a jugar PAR o IMPAR*\033[m')
print('=*=' * 30)
c = 0
while True:
    j = int(input('Tu jugada: '))   #Se pide la jugada del usuario
    pc = randint(1, 5)   #Se da un rango de 5 a la pc
    s = pc + j   #se suman ambos valores
    respuesta = str(input('¿PAR o IMPAR? [P/I]: ')).upper().strip()[0]   #Se pregunta al usuario si cree que el resultado fue par o impar. Solo se considera un caracter
    if s % 2 == 0 and respuesta in 'Pp':
        print(f'¡ACERTASTE! La PC eligió {pc} y tú elegiste {j}, por lo tanto la suma es {s} y es PAR.')
        c += 1
    elif s % 2 != 0 and pi in 'Ii':
        print(f'¡ACERTASTE! La PC eligió {pc} y tú elegiste {j}, por lo tanto la suma es {s} y es IMPAR.')
        c += 1
    else:
        print(f'¡FALLASTE! La PC eligió {pc} y tú elegiste {j}, por lo tanto la suma es {s}.')
        break
    print('¡Vamos a jugar de nuevo!')
print(f'Obtuviste un total de {c} aciertos.')
print('Fin de la partida')
