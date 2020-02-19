#Se crea una lista de datos de personas, se muestra el total de personas censadas, el promedio de edades, las mujeres y edades por encima del promedio
datos = list()
persona = dict()
suma = promedio = 0
while True:
    persona.clear()
    persona['nombre'] = str(input('Nombre: '))
    persona['sexo'] = str(input('Sexo [F/M]: ')).upper()[0]
    while persona['sexo'] not in 'FM':
        print('Respuesta inválida. Intente nuevamente')
        persona['sexo'] = str(input('Sexo [F/M]: ')).upper()
    persona['edad'] = int(input('Edad: '))
    suma += persona['edad']
    datos.append(persona.copy())
    continuar = str(input('¿Quiere continuar? [S/N]: ')).upper()[0]
    while continuar not in 'SN':
        print('Respuesta inválida. Intente nuevamente')
        continuar = str(input('¿Quiere continuar? [S/N]: ')).upper()
    if continuar in 'N':
        break
print('-=' * 30)
print(f'A) En total tenemos {len(datos)} personas censadas.')
promedio = suma / len(datos)
print(f'B) El promedio de edades es de {promedio: 5.2f} años')
print(f'C) Las mujeres censadas fueron:', end='')
for p in datos:
    if p['sexo'] == 'F':
        print(f"{p['nombre']}", end=' - ')
print()
print('D) Lista de personas que están por encima del promedio de edad: ', end='')
for t in datos:
    if t['edad'] >= promedio:
        print('    ', end='')
        for k, v in t.items():
            print(f'{k} = {v};', end=' ')
        print('')
print('<<TERMINADO>>')
