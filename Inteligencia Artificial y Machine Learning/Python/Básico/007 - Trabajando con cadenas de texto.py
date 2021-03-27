# Trabajando con cadenas de texto
'''
    Metodos 
    Son funciones especiales que solo funcionan con algún tipo de dato en particular.
    Para mandarlas a llamar se usa:
        
        variable.metodo()

    variable.strip(): El método strip eliminará todos los caracteres vacíos que pueda contener la variable.
    variable.lower(): El método lower convertirá a las letras en minúsculas.
    variable.upper(): El método upper convertirá a las letras en mayúsculas.
    variable.capitalize(): El método capitalize convertirá a la primer letra de la cadena de caracteres en mayúscula.
    variable.title(): El método capitalize convertirá a la primer letra de la cadena de cada palabra en mayúscula.
    variable.replace (‘o’, ‘a’): El método replace remplazará un caracterer por otro. En este caso remplazará todas las ‘o’ por el caracter ‘a’.
    Índices: se escriben entre corchetes al lado de la variable y son apuntadores númericos a cada caracterer. Como se ve en el video, cuando utiliza la variable nombre[1] aparece la letra ‘a’ dado que dicha variable tiene almacenada en ese momento la cadena de caracteres ‘facundo’ donde la ‘a’ es el segundo caracter.
    Finalmente, la funcion len() la cual muestra como resultado la cantidad de caracteres que contiene un string, tanto si este está almacenado en una variable como si ingresamos directamente un string para que cuente los caracteres.

    Slices
    Podemos dividir cadenas de texto utilizando slices de la siguiente forma
    Se accede a los índices, en los corchetes colocamos el índice desde donde queremos dividir la cadena colocamos dos puntos y el índice hasta donde queremos dividir.
    También le podemos agregar un tercer valor que es el numero de saltos que va a dar para dividir la cadena es decir si colocamos dos va a ir de dos en dos
'''

nombre = 'miguel soto '
print(f'Nombre: "{nombre}"')

# Ejemplos
print(f'Nombre en mayusculas: "{nombre.upper()}"')
print(f'Nombre en minusculas: "{nombre.lower()}"')
print(f'Nombre capitalizado: "{nombre.capitalize()}"') # solo la primera letra
print(f'Nombre capitalizado: "{nombre.title()}"') # todas las palabras con la primera en mayuscula
print(f'Nombre sin el espacio final: "{nombre.title().strip()}"')
reemplazo = nombre.replace('soto', 'angel')
print(f'Reemplazando letras: {reemplazo}')
print(f'Primeros 6 caracteres de "{nombre}": {nombre[:6].capitalize()}')
print(f'Tamano del texto: {len(nombre)}')