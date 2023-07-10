print ('Programa 14. \nPrograma que indica el costo total de la compra de gasolina\n')
def Programa_14():
    G95 = float(input('Precio de Gasolina de 95: '))
    L95 = float(input('Cantidad de Litros de 95: '))

    CostoSinImpuestos = G95*L95
    CostoTotal = CostoSinImpuestos*1.07
    print('CostoTotal =', round (CostoTotal,2))
    
    print('Fin del programa')
    print('\U0001F600 \n') 
Programa_14()