import os

def menu():

    """Función encargada de presentar el menú de opciones."""

    os.system('cls')

    print("\n1.) Registrar venta\n\n2.) Gestionar Catalogo de productos\n\n3.) Generar Factura Electronica.\n")

    while True: 

        try:

            option = int(input("Selecciona opción: "))

            print()

            if option > 0 and option < 4:

                return option
            
            else:

                print("\nRango no permitido!\n")
            
        except ValueError as vl:

            print("\nSolo se Permiten Caractfdseres numéricos!\n")


def menuVentas():

    """Función encargada de retornar la selección
    del menú de ventas"""

    os.system('cls')

    print("1.) Comprar\n\n2.) Cantidades vendidas\n\n3.) Salir\n")

    while True: 

        try:

            option = int(input("Selecciona opción: "))

            if option > 0 and option < 4:

                return option
            
            else:

                print("\nRango no permitido!\n")
            
        except ValueError as vl:

            print("\nSolo se Permiten Caracteres numéricos!\n")




def menuInventory():

    """Función encargada de retornar la selección del menú
    de inventario."""

    os.system('cls')

    print("1.) Agregar Producto\n\n2.) Mostrar Inventario\n\n3.) Salir\n")

    while True: 

        try:

            option = int(input("Selecciona opción: "))

            if option > 0 and option < 4:

                return option
            
            else:

                print("\nRango no permitido!\n")
            
        except ValueError as vl:

            print("\nSolo se Permiten Caracteres numéricos!\n")



