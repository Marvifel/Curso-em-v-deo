#Este programa posibilita el cálculo del Índice de Masa Corporal (IMC) de los usuarios e indica si está en su peso ideal
print('-' * 20)
print('Calculadora de IMC')
print('-' * 20)
p = float(input('Escribe tu peso: '))
e = float(input('Ecribe tu estatura: '))
imc = p / e ** 2
if imc < 18.5:
    print(f'Tu IMC es {imc:.1f} lo cual indica que estás por \033[1;37mDebajo del Peso\033[m')
elif imc <= 25:
    print(f'Tu IMC es {imc:.1f} lo que indica que estás en tu \033[1;36;40mPeso Ideal\033[m')
elif imc <= 30:
    print(f'Tu IMC es {imc:.1f} lo que indica que estás en el rango de \033[1;37mSobrepeso\033[m')
elif imc <= 40:
    print(f'Tu IMC es {imc:.1f} lo que indica que estás en el rango de \033[1;37mObesidad\033[m')
else:
    print(f'Tu IMC es {imc:.1f} y eso te ubica en el rango de \033[1;37mObesidad Mórbida\033[m')
