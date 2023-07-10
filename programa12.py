print('Programa 12. \nPrograma que calcule el interes a pagar por un prestamo\n')
def Programa_12():
    m = float(input('Escribe el valor de m: '))
    t = float(input('Escribe el valor de t: '))
    p = float(input('Escribe el valor de p: '))

    F = m * t * p

    DR = round(F,2)

    print('El resultado es =', DR)
    
    print('Fin del programa')
    print('\U0001F600 \n')
Programa_12()