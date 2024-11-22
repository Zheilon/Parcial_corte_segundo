from datetime import datetime

class GenerarFactura:

    def __init__(self, producto, nombre, cantidad, precio, subtotal):

        self.producto = producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.subtotal = subtotal

    def subtotal(self, listObjs):

        acum = 0

        for z in range(len(listObjs)):

    def producto(self):

        print("Factura Electronica")

        print(f"Fecha: {datetime.now().strftime("%d%m%Y")}")
        
        for z in range(len(self.listClase)):

            for w in z:

                print(f"{z + 1}. {w} ")