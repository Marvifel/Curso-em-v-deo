def voto(a):
    from datetime import date
    edad = date.today().year - a
    if edad < 18:
       return f'Con {edad} años: NO VOTA.'
    elif 18 <= edad < 65:
        return f'Con {edad} años: VOTO OBLIGATORIO.'
    else:
        return f'Con {edad} años: VOTO OPCIONAL.'


e = int(input('¿Cuál es su año de nacimiento?: '))
print(voto(e))
