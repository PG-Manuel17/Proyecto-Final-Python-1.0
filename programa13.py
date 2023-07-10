print ('Programa 13. \n Programa que calcule el salario neto \n')
def Programa_13():
    SAB = float(input('Valor de Salario bruto'))

    SeguroSocial = SAB * 0.0514
    SeguroEducativo = SAB * 0.02
    CuotaPrestamo = 50
    SalarioNeto = SAB - SeguroSocial - SeguroEducativo - CuotaPrestamo

    print('El salario neto es =', round (SeguroSocial,2))
    print('El salario neto es =', round (SeguroEducativo,2))
    print('El salario neto es =', round (CuotaPrestamo,2))
    print('El salario neto es =', round (SalarioNeto,2))
    
    print('Fin del programa')
    print('\U0001F600 \n')
Programa_13()