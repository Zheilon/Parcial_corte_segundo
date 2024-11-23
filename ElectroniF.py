from datetime import datetime

class GenerarFactura:

    def __init__(self, producto, nombre, cantidad, precio, subtotal):

        self.producto = producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.subtotal = subtotal

    def producto(self, listObjs):

        print("Factura Electronica")

        print(f"Fecha: {datetime.now().strftime("%d%m%Y")}")
        
        for z in range(len(listObjs)):

            for w in z:

                print(f"{z + 1}. {w} ")