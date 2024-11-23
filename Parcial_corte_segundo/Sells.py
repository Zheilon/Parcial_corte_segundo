from Inventory import *
from tabulate import tabulate
import os

matrixCantidadVendida = []

def agregarVenta():

    """Función encargada de realizar la compra, y interactuar con la matriz del archivo: Inventory.py."""

    os.system('cls')

    print("\nProductos disponibles!\n")

    showTable()

    codeProduct = str(input("Selecciona código de producto a comprar: ")).upper()

    cantidadCompra = int(input("Ingresa la cantidad que deseas comprar: "))

    for z in range(len(inventoryMatrix)):

        if inventoryMatrix[z][0] == codeProduct:

            if inventoryMatrix[z][3] > cantidadCompra:

                inventoryMatrix[z][3] -= cantidadCompra

                cantidadVent(codeProduct, cantidadCompra)


def cantidadVent(code, cantidad):

    if not matrixCantidadVendida:

        matrixCantidadVendida.append([code, cantidad])

    else:

        for z in range(len(matrixCantidadVendida)):

            for m in range(len(matrixCantidadVendida[0])):

                if matrixCantidadVendida[z][0] != code:

                    matrixCantidadVendida.append([code, cantidad])

                else:

                    matrixCantidadVendida[z][1] += cantidad


def mostrarCantidadVendida():

    """Función encargada de mostrar la cantidad vendida de productos."""

    header = ["Código", "Cantidad Vendida"]

    print(tabulate(matrixCantidadVendida, headers=header, tablefmt="fancy_grid"))