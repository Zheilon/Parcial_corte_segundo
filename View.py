def menu():

    """Función encargada de presentar el menú de opciones."""

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

    print("1.) Comprar\n\n2.) Cantidades vendidas\n\n3.) Agregar nuevos productos")

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

    print("1.) Agregar Producto\n\n2.) Mostrar Inventario\n")

    while True: 

        try:

            option = int(input("Selecciona opción: "))

            if option > 0 and option < 3:

                return option
            
            else:

                print("\nRango no permitido!\n")
            
        except ValueError as vl:

            print("\nSolo se Permiten Caracteres numéricos!\n")

