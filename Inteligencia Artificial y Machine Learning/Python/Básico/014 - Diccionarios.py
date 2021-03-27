# Diccionarios
'''
    Son una estructura de datos mutable las cuales almacenan diferentes tipos de valores sin darle importancia a su orden. 
    Identifican a cada elemento por una clave (Key). 
    Se escriben entre {}.

    Operaciones:
    .keys() —> Retorna la clave de nuestro elemento
    .values()—> Retorna una lista de elementos (valores del diccionario)
    .items() —> Devuelve lista de tuplas (primero la clave y luego el valor)
    .clear() —> Elimina todos los items del diccionario
    .pop(“n”) —> Elimina el elemento ingresado
'''

# Definiendo diccionarios
def main():
    diccionario = {
        'nombre': 'Miguel',
        'edad': 24,
        'pais': 'Mexico',
    }

    caballeros_dorados = {
        'aries': 'mu',
        'tauro': 'aldebaran',
        'cancer': 'deadmask',
        'geminis': 'saga',
        'leo': 'aioria',
        'virgo': 'shaka',
        'libra': 'dohko',
        'sagitario': 'aioros',
        'escorpion': 'milo',
        'capricornio': 'shura',
        'acuario': 'camus',
        'piscis': 'afrodita',
    }

    print('Nombre:', diccionario['nombre'])

    # Acceder a las keys de nuestro diccionario
    for caballeros in caballeros_dorados.keys():
        print(caballeros)

    # Acceder a los valores corresponientes de las keys del diccionario
    for caballeros in caballeros_dorados.values():
        print(caballeros)
    
    # Acceder al item completo del diccionario
    for llave, valor in diccionario.items():
        print(f'{llave} -> {valor}')


if __name__ == '__main__':
    main()