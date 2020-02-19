dato = []
datos = []
gor = fla = 0
while True:
    dato.append(str(input('Nombre: ')))
    dato.append(float(input('Peso (en kg): ')))
    if len(datos) == 0:
        gor = fla = dato[1]   #Cuando la lista datos está vacía, el primer peso registrado es tanto gordo como flaco 
    else:
        if dato[1] > gor:
            gor = dato[1]   #El primer peso pasa a ser el mayor
        if dato[1] < fla:
            fla = dato[1]   #El primer peso pasa a se rel menor
    r = str(input('¿Quiere continuar? [S/N]: '))
    datos.append(dato[:])   #Se copia la lista dato en datos
    dato.clear()   #Se limpia la lista dato para reiniciar el proceso tantas veces como sea necesario
    if r in 'Nn':
        break
print('=*' * 30)
print(f'En total, fueron censadas {len(datos)} personas')
print(f'El mayor peso fue de {gor}kg. Las personas con ese peso o más fueron: ', end='')
for p in datos:
    if p[1] == gor:
        print(f'[{p[0]}]', end='')
print()
print(f'El menor peso fue de {fla}kg. Las personas que pesaron eso o menos fueron: ', end ='')
for p in datos:
    if p[1] == fla:
        print(f'[{p[0]}]', end='')
print()
