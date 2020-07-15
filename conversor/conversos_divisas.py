import divisas as div
# Las divisas están generadas en otro modulo

def cambio_divisa(uyu, moneda):
    return round(uyu / moneda, 2)


def main():
    menu = """ Bienvenido al conversor de divisas extranjeras a pesos uruguayos, 
    donde usted podrá ccalcular su salario en las monedas de la región. 
    Por favor, ingrese las siguientes opciones: 
    1 - UYU a USD
    2 - UYU a ARS
    3 - UYU a RLB
     
    """
    opcion = input(menu)
    if opcion == '1':
        uyu = int(input('Ingrese el monto de su salario: '))
        moneda = div.dolar
        cambio = cambio_divisa(uyu, moneda)
        print(f'Su salario de ${uyu} UYU equivale a ${cambio} dólares')
    elif opcion == '2':
        uyu = int(input('Ingrese el monto de su salario: '))
        moneda = div.peso_argentino
        cambio = cambio_divisa(uyu, moneda)
        print(f'Su salario de ${uyu} UYU equivale a ${cambio} pesos argentinos')
    elif opcion == '3':
        uyu = int(input('Ingrese el monto de su salario: '))
        rlb = div.real
        cambio = cambio_divisa(uyu, moneda)
        print(f'Su salario de ${uyu} UYU equivale a ${cambio} dólares')

    else:
        print("Ingrese opción válida.")
    

if __name__ == '__main__':
    main()