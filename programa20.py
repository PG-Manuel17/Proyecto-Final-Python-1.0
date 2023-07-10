print ('Programa 20. \nPrograma que devuelve el salario neto a pagar \n')
def Programa_20():
    Salario = input('Valor de Salario bruto: ')
    SB = float(Salario)

    SeguroSocial = SB * 0.08
    SeguroEducativo = SB * 0.02
    Impuestos = SB * 0.15
    Prestamo = 100
    SalarioNeto = SB - SeguroSocial - SeguroEducativo - Impuestos - Prestamo

    print('SeguroSocial =', round (SeguroSocial,2))
    print('SeguroEducativo =', round (SeguroEducativo,2))
    print('Impuestos =', round (Impuestos,2))
    print('Prestamo =', round (Prestamo,2))
    print('El salario neto es =', round (SalarioNeto,2))
    
Programa_20()