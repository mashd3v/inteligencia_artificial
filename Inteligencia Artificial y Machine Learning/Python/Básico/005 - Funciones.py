# Fucniones
'''
    Funciones: codigo que puedes reutilizar.
    Las funciones se construyen de la siguiente manera:
        
        def nombre_funcion():
            desarrollo de la funcion.

    Los nombres de las funciones se escriben siempre en minusculas, nunca con numeros y siempre se separan con guion bajo.
    Parametros: variables que voy a tener disponibles para usarla dentro de la función.
'''
# Ejemplos:
def imprimir_mensaje(nombre):
    print(f'Hola {nombre}, buen dia')

def conversacion(nombre, mensaje):
    imprimir_mensaje(nombre)
    print(mensaje)
    print('Adios')

if __name__ == '__main__':
    nombre = input('Escribe tu nombre: ')
    opcion  = int(input ('Elige una opcion (1, 2, 3): '))
    
    if opcion ==1:
        conversacion(nombre, 'Elegiste la opcion 1')
    elif opcion == 2:
        conversacion(nombre, 'Elegiste la opcion 2')    
    elif opcion == 3:
        conversacion(nombre, 'Elegiste la opcion 3') 
    else:
        print('Escribe una opcion correcta')