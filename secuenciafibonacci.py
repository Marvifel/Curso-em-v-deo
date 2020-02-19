print('-' * 30)
print('\033[1;36mSecuencia de Fibonacci\033[m')
print('-' * 30)
fib = int(input('Cantidad de términos de la secuencia: '))
t1 = 0
t2 = 1
print('~' * 40)
print(f'{t1} -> {t2}', end='')
c = 3   
while c <= fib:    
    t3 = t1 + t2
    print('-> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    c +=1
print('-> FIN')
