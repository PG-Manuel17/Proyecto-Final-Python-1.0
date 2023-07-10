print('Programa 15. \nPrograma que devuelve el valor total de los productos a comprar')
def Programa_15():
    precio1 = float(input('articulo1: '))
    precio2 = float(input('articulo2: '))
    precio3 = float(input('articulo3: '))

    total1 = precio1 + precio2 + precio3
    total2 = total1 * 1.07
    RD_1 = round(total1,2)
    RD_2 = round(total2,2)
    print('total sin impuesto =', RD_1)
    print('total con impuesto =', RD_2)
    
    print('Fin del programa')
    print('\U0001F600 \n')


Programa_15()