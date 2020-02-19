#Este programa crea un diccionario con los datos de los jugadores y una lista con los goles. Al final muestra detalles de cuangtos goles y el total 
jugador = dict()
goles = list()
jugador['nombre'] = str(input('Nombre del jugador: '))
partidos = int(input(f"¿Cuántos partidos jugó {jugador['nombre']}?: "))
for i in range(0, partidos):
    goles.append(int(input(f'¿Cuántos goles en el partido {i + 1}?: ')))
jugador['goles'] = goles
jugador['total'] = sum(goles)
print('-=' * 30)
print(jugador)
print('-=' * 30)
for k, v in jugador.items():
    print(f'El campo {k} tiene el valor {v}.')
print('-=' * 30)
print(f'El jugador {jugador["nombre"]} jugó {len(jugador["goles"])} partidos.')
for i in range(len(goles)):
    print(f'   => En el partido {i + 1}, hizo {goles[i]} goles.')
print(f'Fue un total de {jugador["total"]} goles.')
