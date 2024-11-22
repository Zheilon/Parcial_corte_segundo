from Inventory import *

def agregarVenta():

    print("\nProductos disponibles!\n")

    showTable()

    codeProduct = str(input("Selecciona código de producto a comprar: ")).upper()

    cantidadCompra = int(input("Ingresa la cantidad que deseas comprar: "))

    for z in range(len(inventoryMatrix)):

        for w in range(len(inventoryMatrix[0])):

            if inventoryMatrix[z][w] == codeProduct and w == 3:

                if inventoryMatrix[z][w] > 0:

                    inventoryMatrix[z][w] -= cantidadCompra