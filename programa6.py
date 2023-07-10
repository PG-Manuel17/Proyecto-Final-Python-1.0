print('Programa 6. \n Para calcular el area de un trapesio\n')
def Programa_6():
    Base1 = float(input('Escribe el valor de la Base 1: '))
    Base2 = float(input('Escribe el valor de la Base 2: '))
    Altura = float(input('Escribe el valor de la Altura: '))

    Area = ((Base1 + Base2)* Altura)/2

    AR = round(Area,2)

    print('El area de un trapecio es =', AR)
    print('Fin del programa')
    print('\U0001F600 \n')
Programa_6()