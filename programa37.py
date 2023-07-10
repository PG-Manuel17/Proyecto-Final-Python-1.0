def Programa_37():
    value = 1
    while value <= 5:
        print(value)
        value = value + 1
        print('Programa 34 . \nPrograma que indica de 3 valores el numero mayor\n')

        a = float(input('Escriba valor1: '))
        b = float(input('Escriba valor2: '))
        c = float(input('Escriba valor3: '))

        if a > b and a > c:
           print('El numero mayor es a = ', a)
        if b > a and b > c:
           print('El numero mayor es b = ', b)
        if c > a and c > b:
           print('El numero mayor es c = ', c)
           
    print('Fin del programa')
    print('\U0001F618\n')
Programa_37()