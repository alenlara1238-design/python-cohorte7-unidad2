from clases.mision import Mision


class FotografiaAerea(Mision):
    def __init__(self, codigo, cliente, piloto, cantidad, resolucion):
        super().__init__(codigo, cliente, piloto)
        self.cantidad = cantidad
        self.resolucion = resolucion

    def ejecutar(self):
        self.mostrar_informacion()
        print("ejecutando misión de fotografia aerea")
        print("finalalizando mision de fotografia")