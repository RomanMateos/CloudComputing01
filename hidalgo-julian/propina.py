
while True:
    try:
        total_cuenta = int(input('Ingrese el total de su cuenta: '))
        porcentaje = int(input('Ingrese el porcentaje de la propina que desea dar: '))
        total_pagar = ((total_cuenta * porcentaje) / 100) + total_cuenta
        print(f'El valor total a pagar es {int(total_pagar)}')
        break
    
    except:
        print('Porfavor ingresa un valor valido')
