from Inventory import *

matrixCantidadVendida = []

def agregarVenta():

    print("\nProductos disponibles!\n")

    showTable()

    codeProduct = str(input("Selecciona código de producto a comprar: ")).upper()

    cantidadCompra = int(input("Ingresa la cantidad que deseas comprar: "))

    for z in range(len(inventoryMatrix)):

        for w in range(len(inventoryMatrix[0])):

            if inventoryMatrix[z][0] == codeProduct and inventoryMatrix[z][3] > cantidadCompra:

                inventoryMatrix[z][3] -= cantidadCompra

                cantidadVent(codeProduct, cantidadCompra)


def cantidadVent(code, cantidad):

    if not matrixCantidadVendida:

        matrixCantidadVendida.append([code, cantidad])

    else:

        for z in range(len(matrixCantidadVendida)):

            for w in range(len(matrixCantidadVendida[0])):

                if matrixCantidadVendida[z][0] != code:

                    matrixCantidadVendida.append([code, cantidad])

                else:

                    matrixCantidadVendida[z][1] += cantidad


def mostrarCantidadVendida():

    header = ["Código", "Cantidad Vendida"]

    print(tabulate(matrixCantidadVendida, headers=header, tablefmt="fancy_grid"))