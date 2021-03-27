# Programa 1: Conversor de monedas
'''
    Problema: 
        Se nos pide realizar un conversor de monedas especificas a dolares.
        Las monedas son: pesos colombianos, argentinos y mexicanos.
        Se requiere modularidad (por funcion(es)) para realizar dichas conversiones.
'''


def conversor_de_moneda_a_dolar(tipo_moneda, valor_dolar):
    pesos = float(input(f'Cuantos {tipo_moneda} tienes? '))
    dolares = round((pesos / valor_dolar), 2)
    print(f'{pesos} {tipo_moneda} equivalen a {dolares} dolares')  

if __name__ == '__main__':
    try:
        moneda = int(input('''
        Ingresa el indice de la moneda que quieres convertira  dolar:
            [1] Moneda Colombiana a Dolar
            [2] Moneda Argentina a Dolar
            [3] Moneda mexicana a Dolar
        Selecciona: '''))
        if moneda == 1:
            conversor_de_moneda_a_dolar('pesos colombianos', 3875)
        elif moneda == 2:
            conversor_de_moneda_a_dolar('pesos argentinos', 65)
        elif moneda == 3:
            conversor_de_moneda_a_dolar('pesos mexicanos', 24)
        else:
            print('Ingresa una opcion valida')            
    except:
        print('* * * * * * E R R O R * * * * * *')
        print('Por favor ingresa solo valores numericos')