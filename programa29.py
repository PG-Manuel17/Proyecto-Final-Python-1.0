def Programa_29():
    value = 1
    while value <= 5:
        print(value)
        value += 1
        print('Programa 28. \nEn ciclo While hasta 5 veces(determina la nota)\n')
        Valor = float(input('Escribe el valor: '))
        if Valor >= 90:
            print('Es A')        
        elif Valor >= 80 and Valor <90:
            print('Es B')
        if Valor >= 70 and Valor < 80:
            print('Es C')        
        elif Valor >= 60 and Valor < 70:
            print('Es D')
        if Valor < 60:
            print('Es F')        
        print('Fin del programa')
        print('\U0001F618')
Programa_29()