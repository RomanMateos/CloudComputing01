print('-----Cuenta-----')
cuenta = int(input('Ingrese el total de su cuenta por favor: '))
propina = int(input('Ingrese porcentaje de propina (sugerido 10%): '))

propina_pesos = (cuenta * propina) / 100

cuenta_total = cuenta + propina_pesos

print(f'Propina = {propina_pesos:.2f}$')
print(f'Total cuenta con propina = {cuenta_total:.1f}$')

