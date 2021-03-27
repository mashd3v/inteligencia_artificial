# Programa 2: Palindromo
'''
    Problema:
    Dada una cadena de texto, definir si esta es un palindromo o no.
    Un palindromo es un texto que se lee de la misma manera de izquierda a derecha como de derecha a izquierda.
'''

def es_palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else: 
        return False


def ejecutar():
    palabra = input('Escribe una palabra: ')
    palindromo = es_palindromo(palabra)
    if palindromo == True:
        print(f'{palabra} es un palindromo')
    else:
        print(f'{palabra} no es un palindromo')


# Entry point o punto de entrada
if __name__ == '__main__': 
    ejecutar()