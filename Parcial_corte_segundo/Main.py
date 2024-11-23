from View import *
from Inventory import *
from Sells import *
from ElectroniF import *

print("ELECTRO MUNDO SAS")

while True:

    option = menu()

    #VENTAS                                                                                    

    if option == 1:

        while True:

            menuVt = menuVentas()

            if menuVt == 1:

                agregarVenta()

            elif menuVt == 2:

                mostrarCantidadVendida()

            elif menuVt == 3:

                pass

            confirm = str(input("Deseas continuar? S / N: "))

            if confirm.upper() == "N":

                break

    #INVENTARIO

    elif option == 2:

        while True:

            menuIn = menuInventory()

            if menuIn == 1:

                addProduct()

            elif menuIn == 2:

                showTable()

            elif menuIn == 3:

                break

            confirm = str(input("Deseas continuar? S / N: "))

            if confirm.upper() == "N":

                break

    elif option == 3:

        pass #Factura

    #Salir

