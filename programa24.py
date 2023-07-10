print('Programa 24. n\ Programa que indica de 3 valores el numero mayor')
def Programa_24():
    a = float(input('Escriba valor1: '))
    b = float(input('Escriba valor2: '))
    c = float(input('Escriba valor3: '))

    if a > b and a > c:
        print('El numero mayor es a =', a)
    if b > a and b > c:
        print('El numero mayor es b =', b)
    if c > a and c > b:
        print('El numero mayor es c =', c)
           
    print('Fin del programa')
    print('\U0001F618\n')
Programa_24()
