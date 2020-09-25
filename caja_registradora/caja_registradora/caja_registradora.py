import Venta
import decimal
import VentaConDescuento
import Producto


ciclo = -1  
subtotal = []
print("ingrese 1 para ingresar un código")
print("ingrese 2 para ingresar un nombre de producto")
print("ingrese 3 para ingresar un precio")
print("ingrese 4 para ingresar una cantidad")
print("ingrese 5 para porcentaje")
print("ingrese 6 para guardar la operación")
while ciclo != 0:
    ciclo = int(input("introduce un número "))    
    if ciclo == 1:
        codigo = input("introduce un código")
        print("el codigo de producto es ",codigo)
        pass
    if ciclo == 2:
        descripcion = input("introduce un nombre del producto")
        print("El nombre del producto es ", descripcion)
        pass
    if ciclo == 3:
        precio = int(input("Introduce un precio"))
        print("El precio del producto es", precio)
        pass
    if ciclo == 4:
        cantidad = int(input("Introduce una cantidad"))
        print("La cantidad es", cantidad)
        pass
    if ciclo == 5:
        porcentaje = input("introduce un porcentaje")
        print("el porcentaje es", porcentaje)
        pass
    if ciclo == 6:
        subtotal.append(precio * cantidad);
        print("total",subtotal)
        print("suma",sum(subtotal))
    print("ingrese 0 para salir del ciclo")
 


   