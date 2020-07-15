import divisas as div
# Las divisas están generadas en otro modulo

def cambio_divisa(uyu, moneda):
    return uyu * moneda


def main():
    menu = """ Bienvenido al conversor de divisas extranjeras a UYU. 
    Por favor, ingrese las siguientes opciones: 
    1 - UYU a USD
    2 - UYU a ARS
    3 - UYU a RLB
     
    """
    uyu = input(menu)
    if uyu == '1':
        moneda = div.dolar
        cambio = cambio_divisa(uyu, moneda)
    elif uyu == '2':
        moneda = div.peso_argentino
        cambio = cambio_divisa(uyu, moneda)
    elif uyu == '3':
        rlb = div.real
        cambio = cambio_divisa(uyu, moneda))
    else:
        print("Ingrese opción válida.")
    

if __name__ == '__main__':
    main()