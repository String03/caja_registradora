class Venta(object):
    """description of class"""
    def __init__(self, precio, cantidad, total):
        self.precio = precio
        self.cantidad = cantidad
        self.total= total

    def __repr__(self):
        return (self.precio, self.cantidad)



    