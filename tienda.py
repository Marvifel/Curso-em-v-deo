print('=*' * 10)
print('Tienda Súper Barata')
print('=*' * 10)
t = c = m = b = 0
k = ''
barato = ''
while True:
    n = str(input('Nombre del producto: '))
    p = float(input('Precio: AR$'))
    k = str(input('¿Quieres continuar? [S/N]: ')).upper().strip()[0]
    t += p
    b += 1
    while k not in 'SsNn':
        k = str(input('¿Quieres continuar? [S/N]: ')).upper().strip()[0]   #si el usuario no responde entre S o N, se le vuelve a solicitar respuesta
    if p > 500:
        c += 1
    if b == 1:
        m = p
        barato = n
    else:
        if p < m:
            m = p
            barato = n
    if k in 'Nn':
        print('-' * 25)
        print('Su compra ha finalizado...')
        print('-' * 25)
        break
print(f'''El total de la compra fue AR${t}
{c} productos costaron más de AR$500
El producto más barato fue {barato} y costó AR${m}
¡Disfrute de sus productos!''')
