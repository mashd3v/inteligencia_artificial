# Programa 5: Generador de contrasenas
'''
    Problema:
    Crear un programa que genere contrasenas el cual incluya:
        - Todas las letras mayusculas y minusculas
        - Numeros del 0 al 9
        - Simbolos
'''

import random

def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    simbolos = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    caracteres = mayusculas + minusculas + numeros + simbolos
    contrasena = []

    for i in range(16):
        caracter_aleatorio = random.choice(caracteres)
        contrasena.append(caracter_aleatorio)

    contrasena = "".join(contrasena)

    return contrasena


def main():
    contrasena = generar_contrasena()
    print(f'Tu nueva contrasena es: {contrasena}')


if __name__ == '__main__':
    main()