from datetime import datetime
from tabulate import tabulate

# Lista para almacenar las facturas en memoria
facturas = []

class GenerarFactura:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.subtotal = self.cantidad * self.precio

    def mostrar_producto(self):
        return [self.nombre, self.cantidad, self.precio, self.subtotal]

def mostrar_detalles(productos):
    print("\nDetalles de los productos comprados:")
    headers = ["Nombre", "Cantidad", "Precio", "Subtotal"]
    table = [producto.mostrar_producto() for producto in productos]
    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

def calcular_totales(productos):
    subtotal = sum(producto.subtotal for producto in productos)
    iva = subtotal * 0.19  # IVA del 19%
    total = subtotal + iva
    return subtotal, iva, total

def guardar_factura(productos, subtotal, iva, total):
    factura = {
        "productos": [producto.__dict__ for producto in productos],
        "subtotal": subtotal,
        "iva": iva,
        "total": total,
        "fecha": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }
    facturas.append(factura)
    print("\nFactura guardada para futuras consultas.")

def mostrar_facturas():
    if not facturas:
        print("No hay facturas guardadas.")
        return

    for i, factura in enumerate(facturas):
        print(f"\nFactura {i + 1}:")
        print(f"Fecha: {factura['fecha']}")
        print("\nDetalles de los productos comprados:")
        headers = ["Nombre", "Cantidad", "Precio", "Subtotal"]
        table = [[p['nombre'], p['cantidad'], p['precio'], p['subtotal']] for p in factura["productos"]]
        print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
        print(f"\nSubtotal: {factura['subtotal']:.2f}")
        print(f"IVA: {factura['iva']:.2f}")
        print(f"Total: {factura['total']:.2f}")

def menu_facturacion():
    productos = []
    while True:
        print("\nMenú de Facturación:")
        print("1. Ingresar producto")
        print("2. Mostrar detalles de la factura")
        print("3. Calcular y mostrar totales")
        print("4. Guardar factura")
        print("5. Mostrar facturas guardadas")
        print("6. Volver al menú principal")
        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
            producto = GenerarFactura(nombre, cantidad, precio)
            productos.append(producto)
        elif opcion == "2":
            if productos:
                mostrar_detalles(productos)
            else:
                print("No hay productos ingresados.")
        elif opcion == "3":
            if productos:
                subtotal, iva, total = calcular_totales(productos)
                print(f"\nSubtotal: {subtotal:.2f}, IVA: {iva:.2f}, Total: {total:.2f}")
            else:
                print("No hay productos ingresados.")
        elif opcion == "4":
            if productos:
                subtotal, iva, total = calcular_totales(productos)
                guardar_factura(productos, subtotal, iva, total)
                productos.clear()  # Limpiar productos después de guardar la factura
            else:
                print("No hay productos ingresados.")
        elif opcion == "5":
            mostrar_facturas()
        elif opcion == "6":
            break
        else:
            print("Opción inválida, por favor ingrese una opción válida.")
