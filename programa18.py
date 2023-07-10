print('Programa 18. \nCalcula el interés compuesto\n')
def Programa_18():
    ci = float(input('Escriba la capital inicial: '))
    i = float(input('Escriba la tasa de interés: '))
    n = float(input('Escriba el número de periodos: '))

    Cf = ci * (1 + i) * n
    CapitalFinal = round(Cf, 2)

    print('La capital final es =', CapitalFinal)
    
    print('Fin del Programa')
    print('\U0001F600\n')
Programa_18()