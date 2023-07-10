print('Programa 7. \nPara calcular el volumen de un prisma rectangular\n')
def Programa_7():
    P1 = input('Escribe el valor de Largo: ')
    P2 = input('Escribe el valor de Ancho: ')
    P3 = input('Escribe el valor de Altura: ')

    Largo = float(P1)
    Ancho = float(P2)
    Altura = float(P3)

    Vol = (Largo * Ancho * Altura)
    VolR= round(Vol,4)

    print('El volumen de un prisma rectangular es = ', VolR)
    print('Fin del programa')
    print('\U0001F600 \n')
Programa_7()