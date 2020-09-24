class Producto(object):
    """description of class"""

    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion


    def __repr__(self):
        return (self.codigo , self.descripcion)





