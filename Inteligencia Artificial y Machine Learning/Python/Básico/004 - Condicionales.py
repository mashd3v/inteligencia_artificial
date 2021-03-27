# Condicionales
'''
    if : si
    elif: en cambio sino (lo podemos usar cuantas veces sean necesarias)
    else: sino
'''
# Ejemplos: 
edad = int(input('Escribe tu edad: '))
if(edad > 17):
    print('Eres mayor de edad, adelante')
else:
    print('Eres menor de edad, no puedes seguir')


numero = int(input('Dame un numero: '))
if numero > 5:
    print(f'{numero} es mayor a 5')
elif numero == 5:
    print(f'{numero} es igual a 5')
else:
    print(f'{numero} es menor a 5')
