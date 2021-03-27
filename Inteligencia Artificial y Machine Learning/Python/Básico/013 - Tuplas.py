# Tuplas
'''
    En Python, una tupla es un conjunto ordenado e inmutable de elementos del mismo o diferente tipo. 
    Las tuplas se representan escribiendo los elementos entre paréntesis y separados por comas. Una tupla puede no contener ningún elemento, es decir, ser una tupla vacía.
    Funciones que aplican a tuplas:
        - len
        - max
        - min
        - sum
        - any
        - all
        - sorted
    Métodos que aplican a tuplas:
        - index
        - count
'''

# Definiendo tuplas
tupla_1 = (11, 2, 30, 4, 52, 6, 70, 8, 9, 100)

print(f'Longitud de la tupla: {len(tupla_1)}')
print(f'Maximo de la tupla: {max(tupla_1)}')
print(f'Minimo de la tupla: {min(tupla_1)}')
print(f'Suma de los valores de la tupla: {sum(tupla_1)}')
print(f'Tupla ordenada: {sorted(tupla_1)}')

# La diferencia del recorrido de una lista y una tupla, es que la tupla sera mas rapido
print('\nRecorrido de una tupla')
for elemento in tupla_1:
    print(elemento)

