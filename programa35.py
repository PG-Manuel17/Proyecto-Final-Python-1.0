def Programa_35():
    print('Programa 35. \nPrograma que se detiene al llegar a 9 en bucle de for\n')
    for i in range (1, 11):
        if i > 5:
            print('mayor a 5')
        elif i < 5:
            print('menor a 5')
        else:
            print('es igual a 5')
        if i == 9:
            break
        
    print('Fin del programa')
    print('\U0001F618\n')
Programa_35()