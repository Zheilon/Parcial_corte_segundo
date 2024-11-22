from View import *
from Inventory import *
from Sells import *
from ElectroniF import *

print("ELECTRO MUNDO SAS")

while True:

    option = menu()

    #VENTAS                                                                                    

    if option == 1:

        menuVt = menuVentas()

        if menuVt == 1:

            agregarVenta()

        elif menuVt == 2:

            mostrarCantidadVendida()

        elif menuVt == 3:


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

