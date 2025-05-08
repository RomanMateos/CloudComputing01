name = str(input('\nIngrese su nombre: '))
age = int(input('\nIngrese su edad: '))

print(f'\n---------Bienvenido {}---------\n' .format(name))
dist = abs(age-100)

if age < 100 and dist > 0:
 print(f'\nLe faltan {} años para llegar a los 100' .format(dist))
else:
 print('Usted ya cumplió los 100 años')

resultado = str(dist)

with open('edad.txt', 'w') as archivo:
 archivo.write('Los años que le faltan para llegar a 100 es: ' + str(dist))

