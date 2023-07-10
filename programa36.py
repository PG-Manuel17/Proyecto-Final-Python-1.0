def Programa_36():
    print('Programa 36. \nCaptura 5 artículos y calcula su 7%\n')

    i = 0
    while i < 5:
        valor = float(input('Escribe el valor del artículo: '))
        impuesto = valor * 0.07
        print('El impuesto del artículo con valor: ', valor, 'es: ', impuesto)
        i += 1

    print('Final del programa')
Programa_36()