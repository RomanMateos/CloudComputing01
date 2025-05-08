print('bienvenido maguito')
Nivel = int(input('ingres su nivel de magia (1-100): '))

if Nivel >= 1 and Nivel <= 20: # se puede colocar nivel <= 20 para simplificar el codigo
    print('nivel de magia Principiante')
elif Nivel > 20 and Nivel <= 50: # es lo mismo para el resto de los niveles
    print('nivel de magia Intermedio')
elif Nivel > 50 and Nivel <= 80:
    print('nivel de magia Avanzado')
elif Nivel > 80 and Nivel <= 100: # aquí podría colocar un else para hablar de los niveles mayores de 80
    print('nivel de magia Maestro')
else:
    print('nivel de magia Inexistente')  
