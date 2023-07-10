print('Programa 19. \nPrograma que devuelve el valor total de los productos con y sin impuestos y el promedio de la compra sin impuestos\n')
def Programa_19():
    valor1 = float(input('articulo1: '))
    valor2 = float(input('articulo2: '))
    valor3 = float(input('articulo3: '))
    valor4 = float(input('articulo4: '))
    valor5 = float(input('articulo5: '))

    total1 = valor1 + valor2 + valor3 + valor4 + valor5
    total2 = total1 * 1.07
    promedio = (valor1 + valor2 +valor3 + valor4 + valor5)/5

    RD1 = round(total1, 2)
    RD2 = round(total2, 2)
    RD3 = round(promedio, 2)

    print('total1 =', RD1)
    print('total2 =', RD2)
    print('promedio =', RD3)

Programa_19()