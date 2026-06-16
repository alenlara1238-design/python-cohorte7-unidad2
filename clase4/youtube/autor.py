class Autor:
    """
        Representa al creador del video
    """
    def __init__(self, nombre, suscriptores, pais, verificado):
        self.nombre = nombre
        self.__suscriptores = suscriptores
        self.pais = pais
        self.verificado = verificado
    
    # Getter: mostrar el dato
    def get_suscriptores(self):
        return self.__suscriptores

    # Setter: modificar (establecer) el dato
    def set_suscriptores(self, cantidad):
        if cantidad >= 0:
            self.__suscriptores += cantidad
        else:
            print("Error: los suscriptores no pueden ser negativos")

    
    def mostrar_info(self):
        print("\n=====Autor======")
        print(f"Nombre: {self.nombre}")
        print(f"Suscriptores: {self.__suscriptores}")
        print(f"País: {self.pais}")
        print(f"Verificado: {self.verificado}")

