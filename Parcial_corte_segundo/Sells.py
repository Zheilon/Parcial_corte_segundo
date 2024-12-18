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

        if inventoryMatrix[z][0] == codeProduct and inventoryMatrix[z][3] > cantidadCompra:

                inventoryMatrix[z][3] -= cantidadCompra

                cantidadVent(codeProduct, inventoryMatrix[z][1], cantidadCompra)


def cantidadVent(code, name, cantidad):

    """Función encargada de registrar las ventas de cada producto."""

    if not matrixCantidadVendida:

        matrixCantidadVendida.append([code, name, cantidad])

    else:

        for z in range(len(matrixCantidadVendida)):

            if matrixCantidadVendida[z][0] != code:

                matrixCantidadVendida.append([code, name, cantidad])

            else:

                matrixCantidadVendida[z][2] += cantidad


def mostrarCantidadVendida():

    """Función encargada de mostrar la cantidad vendida de productos."""

    header = ["Código", "Producto", "Cantidad Vendida"]

    print(tabulate(matrixCantidadVendida, headers=header, tablefmt="fancy_grid"))