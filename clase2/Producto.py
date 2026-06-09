"""
Producto:
- Nombre: obligatorio
- Precio: mayor a cero (sensible: get y set)
- Stock: no negativo (sensible: get y set)
"""

class Producto:
    def __init__(self, nombre, precio, stock):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    def get_precio(self):
        return self.__precio
    
    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("Precio inválido")

    def get_stock(self):
        return self.__stock
    
    def set_stock(self, nuevo_stock):
        if nuevo_stock >= 0:
            self.__stock = nuevo_stock
        else:
            print("Stock negativo no es aceptable")



producto1 = Producto()