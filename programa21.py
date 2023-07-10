print('Programa 21. \nCalcula si una persona paga impuestos\n')
def Programa_21():
    salario = float(input('Escriba el salario: '))

    if salario == 3000:
        impuesto = salario * 1.07
        print('Esta persona debe abonar impuestos',impuesto)
    else:
        print('Esta persona no debe abonar impuestos')
        
    print('Fin del programa')
    print('\U0001F600\n')
Programa_21()