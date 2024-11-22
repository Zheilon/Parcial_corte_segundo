from tabulate import tabulate

inventoryMatrix = []

def addProduct():

    count = int(input("Cuantos productos deseeas ingresar?: "))

    while count > 0:

        codigo = str(input("Ingresa Código unico del producto: ")).upper()

        print()

        nombre = str(input("Ingresa nombre de producto: ")).upper()

        print()

        precio_unitario = int(input("Ingresa precio unitario: "))

        print()

        categoria = categories()

        print()

        cantidadP = int(input("Ingrese Cantidad de producto: "))

        print()

        inventoryMatrix.append([codigo, nombre, precio_unitario, cantidadP ,categoria])

        count -= 1


def showTable():

    """Función encargada de mostrar el inventario"""

    headers = ["Código", "Nombre", "Precio Unitario", "Stock", "Categoria"]

    print(tabulate(inventoryMatrix, headers=headers, tablefmt="fancy_grid"))


def categories():

    """Función encargada de mostrar las categorias y retornar la selección."""

    listC = ["Lína Blanca", "Pequeños Electrodomesticos", "Entretenimiento", "Aires Acondicionadores"]

    print("Categorias:\n")

    for z in range(len(listC)):

        print(f"{z + 1}. {listC[z]}")
    
    print()

    while True:

        try:

            option = int(input("Selecciona opción: "))

            if option > 0 and option < 5:

                return listC[option - 1]
            
            else:

                print("\nRangos no permitidos!\n")

        except ValueError as vl:

            print("\nSolo se permiten caracteres numúricos!\n")