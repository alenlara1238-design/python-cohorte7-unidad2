class AireAcondicionado:
    #constructor
    def __init__(self, marca, modelo, temp):
        self.marca = marca
        self.modelo = modelo
        self.__temp = 24

        #aqui validamos si temp está entre 16 y 30, sino queda en 24
        if 16 <= temp <= 30:
            self.__temp = temp
        else:
            print("temperatura inicial inválida. Se asignó 24°C por defecto")

    # funciones para atributo protegido
    #getter
    def get_temperatura(self):
        return self.__temp
    
    # setter
    def set_temperatura(self, nueva_temperatura):
        if 16 <= nueva_temperatura <= 30:
            self.__temp = nueva_temperatura
            print("Temperatura actualizada")
        else:
            print("Error: la temperatura debe estar 16°C y 30°C")
    
    def aumentar_temp(self):
        if self.__temp < 30:
            self.__temp += 1
        else:
            print("temperatura maxima alcanzada")

    def disminuir_temp(self):
        if self.__temp > 16:
            self.__temp -= 1
        else:
            print("temperatura mínima de 16° alcanzada")

    
    def consultar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"temperatura actual: {self.__temp}")


print("CREANDO AIRE ACONDICIONADO")
aire1 = AireAcondicionado("Samsung", "AT234", 18)
aire1.consultar_info()

aire1.disminuir_temp()
aire1.disminuir_temp()
aire1.disminuir_temp()
aire1.disminuir_temp()
aire1.consultar_info()