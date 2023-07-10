print('Programa 22. \nPrograma que indica la temperatura\n')
temperatura = float(input('Escriba la temperatura: '))

if temperatura < 20:
    if temperatura < 10:
        print('= Nivel azul')
    else:
        print('= Nivel verde')
else:
    if temperatura < 30:
        print('= Nivel naranja')
    else:
        print('= Nivel rojo')
print('Fin del programa')
print('\U0001F600\n')