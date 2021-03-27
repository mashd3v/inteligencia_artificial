# Programa 4: Adivina el numero
'''
    Problema: 
    Realizar un "videojuego"en el cual la computadora genere un numero random y nosotros tratemos de adivinar cual genero.
'''
import random

def main():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Elige un numero del 1 al 100: '))
    
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Elige un numero mas grande')
        else:
            print('Elige un numero mas chico')
        numero_elegido = int(input('Elige otro numero: '))
    print('Acertaste!')


if __name__ == '__main__':
    main() 