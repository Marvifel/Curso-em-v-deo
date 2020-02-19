#Este programa pregunta al usuario de qué manera realizará el pago y calcula el descuento o aumento de acuerdo al caso
p = float(input('Precio normal del producto: '))   #precio
print('''FORMA DE PAGO:
[1] De contado en efectivo o cheque
[2] De contado con TDC
[3] En 2 cuotas con TDC
[4] En 3 o más cuotas con TDC''')
opción = int(input('¿Cuál es su opción de pago?: '))
if opción == 1:
    d = p * 0.10   #Descuento del 10%
    tp = p - d   #total a pagar
    print(f'Usted recibirá un descuento de 10% en el producto, lo que equivale a Bs.{d:.2f}. Total a pagar Bs.{tp:.2f}')
elif opción == 2:
    tp = p - (p * 0.05)   #total a pagar con descuento de 5%
    print(f'Usted recibirá un descuento de 5% en su compra. Total a pagar Bs.{tp:.2f}')
elif opción == 3:
    cuotas = p / 2   #En 2 cuotas
    print(f'Usted debe pagar el precio normal del producto en dos cuotas de Bs.{cuotas}. Total a pagar Bs.{p:.2f}')
elif opción == 4:
    tp = p * 0.20   #Total a pagar con 20% de aumento
    ncuotas = int(input('¿En cuántas cuotas?: '))   #Solicita al usuario el número de cuotas
    cuotas = tp / ncuotas   #Calcula el valor de las cuotas
    print(f'Usted deberá pagar 20% sobre el precio del producto, lo que equivale a Bs.{tp:.2f} en {ncuotas} cuotas de Bs.{cuotas:.2f}')
else:
    print('Opción inválida. Intenta nuevamente.')
print('\033[7;30m¡Gracias por su compra!\033[m')
