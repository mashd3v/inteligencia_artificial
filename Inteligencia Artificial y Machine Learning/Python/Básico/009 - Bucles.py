# Bucles
'''
    Un bucle es un ciclo continuo en todos los lenguajes de programacion, que nos permite iterar sobre nuestros pasos, imagina un contador cíclico (1,2,3,4,5,6...) donde puedes agregar un paso mas sobre tu programa principal.
    Bucles de la vida real:
        - Despertar
        - Comer
        - Dormir

    While
    Un bucle while permite repetir la ejecución de un grupo de instrucciones mientras se cumpla una condición (es decir, mientras la condición tenga el valor True).
    La sintaxis del bucle while es la siguiente:

        while condicion:
            cuerpo del bucle

    Python evalúa la condición:
    Si el resultado es True, se ejecuta el cuerpo del bucle. Una vez ejecutado el cuerpo del bucle, se repite el proceso (se evalúa de nuevo la condición y, si es cierta, se ejecuta de nuevo el cuerpo del bucle) una y otra vez mientras la condición sea cierta.
    Si el resultado es False, el cuerpo del bucle no se ejecuta y continúa la ejecución del resto del programa.

    For
    El bucle for se utiliza para recorrer los elementos de un objeto iterable (lista, tupla, conjunto, diccionario, …) y ejecutar un bloque de código. 
    En cada paso de la iteración se tiene en cuenta a un único elemento del objeto iterable, sobre el cuál se pueden aplicar una serie de operaciones.
    La instrucción “continue” en Python devuelve el control al comienzo del ciclo while o ciclo for. La instrucción “continue” rechaza todas las declaraciones restantes en la iteración actual del ciclo y mueve el control de regreso a la parte superior del ciclo.
    La instrucción “break” en Python termina el ciclo actual y reanuda la ejecución en la siguiente instrucción
'''

def ciclo_while(limite):
    contador = 0
    while contador < limite + 1:
        potencia_cuadrada(contador)
        contador += 1

def ciclo_for(limite):
    for numero in range(limite + 1):
        potencia_cuadrada(numero) 


def potencia_cuadrada(numero):
    print(f'{numero}^2 = {numero ** 2}')


if __name__ == '__main__':
    print('Ciclo while: ')
    ciclo_while(10)

    print('\nCiclo for:')
    ciclo_for(10)