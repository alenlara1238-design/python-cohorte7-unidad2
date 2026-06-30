#import Mision from mision

from clases import Mision


class EntregaMedicamentos(Mision):
    def __init__(self, codigo, cliente, piloto, peso, destino):
        super().__init__(codigo, cliente, piloto)
        self.peso = peso
        self.destino = destino

    def ejecutar(self):
        self.mostrar_informacion()
        print("Ejecutando misión de entrega")
        print("finalizando la misión de entrega")
