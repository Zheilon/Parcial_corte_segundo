from View import *
from Inventory import *
from Sells import *

while True:

    option = menu()

    #VENTAS                                                                                    

    if option == 1:

        menuVt = menuVentas()

        if menuVt == 1:

            agregarVenta()

        elif menuVt == 2:

            pass

        elif menuVt == 3:

            pass

    #INVENTARIO

    elif option == 2:

        menuIn = menuInventory()

        if menuIn == 1:

            addProduct()

        elif menuIn == 2:

            showTable()

    elif option == 3:

        pass #Factura

    #Salir

