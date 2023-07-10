print('Programa 40. \nPrograma que suma los numeros pares entre 1 y 20\n')
def Programa_40(s):
    suma = 0
    for i in range(1, s + 1):
        if i % 2 == 0:
            suma += i
    return suma

print(Programa_40(20))
print('Fin del programa')
print('\U0001F917 \n')