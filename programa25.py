print('Programa 25. \nPrograma que calcula descuentos\n')
def Programa_25():
    Producto = float(input('Escribe el valor del producto: '))
    Descuento = float(input('Escribe el porcentaje de descuento: '))

    Descuento = (Descuento * Producto) / 100
    ValorFinal = Producto - Descuento

    RD = round(ValorFinal, 2)
    print('El precio final es = ', RD)

    if ValorFinal < 50:
        print('Oferta Especial')
    print('Fin del programa')
    print('\U0001F917\n')
Programa_25()
