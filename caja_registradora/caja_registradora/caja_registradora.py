import Venta
import decimal
import VentaConDescuento
import Producto


ciclo = -1  

print("ingrese 1 para ingresar un código")
print("ingrese 2 para ingresar un nombre de producto")
print("ingrese 3 para ingresar un precio")
print("ingrese 4 para ingresar una cantidad")
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
        precio = input("Introduce un precio")
        print("El precio del producto es", precio)
        pass
    if ciclo == 4:
        cantidad = input("Introduce una cantidad")
        print("La cantidad es", cantidad)
        pass
    print("ingrese 0 para salir del ciclo")
    
       
   