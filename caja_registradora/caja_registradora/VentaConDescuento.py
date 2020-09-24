from Venta import Venta
class VentaConDescuento(Venta):
    def __init__(self,descuento,precio,cantidad,total):
        self.descuento = descuento
        self.precio = precio
        self.cantidad = cantidad
        self.total = total


    def __repr__(self):
        return self.descuento