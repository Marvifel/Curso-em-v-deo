#Este programa verifica si una frase escrita por el usuario es palíndromo o no
f = str(input('Escribe una frase: ')).strip().upper()   #Nos aseguramos de quitar los espacios y colocar toda la frase en mayúsculas
frase = f.split()   #Creamos una lista cuyos elementos son las letras de la frase
junto = ''.join(frase)   #Creamos una lista cuyo unico elemento es toda la frase junta
inv = junto[::-1]   #Invertimos el orden de la lista
inverso = ''   #Lista vacía
print(f'Tu frase sin espacios es {junto}.')
print(f'Invertida resulta {inv}.')
for l in range(len(junto) - 1, -1, -1):   #Iteramos y agregamos los elementos a la lista inverso
    inverso += junto[l]
if inverso == junto:
    print('Tenemos un palíndromo')
else:
    print('No es un palíndromo')
