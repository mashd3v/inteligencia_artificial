# Listas
'''
    Las listas nos permiten guardar múltiples valores en una sola variable. Estas listas, en Python, nos permiten guardar elementos del mismo tipo o diferentes, por lo que podemos tener strings, números enteros y decimales juntos en una misma variable. Las listas también son conocidas como “arrays” en otros lenguajes programación.

    append(): Este método agrega un elemento al final de una lista.
    count(): Este método recibe un elemento como argumento, y cuenta la cantidad de veces que aparece en la lista.
    extend(): Este método extiende una lista agregando un iterable al final.
    index(): Este método recibe un elemento como argumento, y devuelve el índice de su primera aparición en la lista.
    insert(): Este método inserta el elemento x en la lista, en el índice i.
    pop(): Este método devuelve el último elemento de la lista, y lo borra de la misma.
    remove(): Este método recibe como argumento un elemento, y borra su primera aparición en la lista.
    reverse(): Este método invierte el orden de los elementos de una lista.
    sort(): Este método ordena los elementos de una lista.
    Convertir a listas: Para convertir a tipos listas debe usar la función list() la cual esta integrada en el interprete Python.
'''

# Definiendo listas
numeros = [1, 3, 5, 7]
objetos = ['Holas', 3, 4.6, True]

print(f'Llamar al arreglo numeros:{numeros} en la posicion 1: {numeros[1]}')

print(f'\nAgregar 2 al final de numeros:{numeros}')
numeros.append(2)
print(f'Numeros:{numeros}')

print(f'\nEliminar la posicion 2 del arreglo numeros:{numeros}')
numeros.pop(2)
print(f'Numeros:{numeros}')

print(f'\nRecorriendo la lista objetos:{objetos}')
for elemento in objetos:
    print(elemento)

print(f'\nMostrar la lista objetos:{objetos} invertida: {objetos[::-1]}')

print(f'\nMostrar solo los elementos de numeros:{numeros} a partir de la posicion 2: {numeros[2:]}')

print(f'Sumar numeros:{numeros} mas objetos:{objetos}: {numeros + objetos}')