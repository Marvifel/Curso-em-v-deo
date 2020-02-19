#Crear una matríz en la que el usuario escriba cada elemento de fila y columna, mostrar la suma de todos los valores pares, la suma de los valores de la tercera columna y el mayor valor de la segunda fila.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = c3 = f2m = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Escribe un número para la posición [{l},{c}]: '))
print('-=' * 40)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
    print()
print('-=' * 40)
print(f'La suma de todos los valores pares es {par}.')
for l in range(0, 3):
    c3 += matriz[l][2]
print(f'La suma de los valores de la tercera columna es {c3}')
for c in range(0, 3):
    if c == 0:
        f2m = matriz[1][c]
    elif matriz[1][c] > f2m:
        f2m = matriz[1][c]
print(f'El mayor valor de la segunda fila es {f2m}')
