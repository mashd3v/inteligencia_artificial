# Operadores logicos
'''
    and: devuelve Verdadero si las todas las variables que estoy comparando son Verdaderas
    or: Devuelve verdadero si al menos una de las variables que estoy comparando es verdadera.
    not: Invertir el valor boleano.
    ==: Compara dos variables/valores, y devuelve verdadero si son iguales y falso si no lo son
    !=: Compara dos variables/valores, devuelve verdadero si son diferentes o falso de lo contrario
    >: Compara dos variables/valores, devuelve verdadero si el primero es mayor que el segundo.
    <: Compara dos variables/valores, devuelve verdadero si el primero es menor que el segundo.
    >=: Compara dos variables/valores, devuelve verdadero si el primero es mayor o igual que el segundo.
    <=: Compara dos variables/valores, devuelve verdadero si el primero es menor o igual que el segundo.
'''
# Definimos primero variables que utilizaremos para los ejemplos
es_estudiante = True
trabaja = False
numero_1 = 5
numero_2 = 6
print('Variables:')
print(f'Es estudiante: {es_estudiante}')
print(f'Trabaja: {trabaja}')
print(f'Numero 1: {numero_1}')
print(f'Numero 2: {numero_2}')

# Ejemplos: 
print('\nEjemplos:')
print(f'Es estudiante y (and) trabaja: {es_estudiante and trabaja}')
print(f'Es estudiante o (or) trabaja: {es_estudiante or trabaja}')
print(f'No (not) trabaja: {not trabaja}')
print(f'{numero_1} es igual (==) a {numero_2}: {numero_1 == numero_2}')
print(f'{numero_1} es diferente (!=) a {numero_2}: {numero_1 != numero_2}')
print(f'{numero_1} es mayor (>) a {numero_2}: {numero_1 > numero_2}')
print(f'{numero_1} es menor (<) a {numero_2}: {numero_1 < numero_2}')
print(f'{numero_1} es mayor o igual (>=) a {numero_2}: {numero_1 >= numero_2}')
print(f'{numero_1} es menor o igual (<=) a {numero_2}: {numero_1 <= numero_2}')

