"""
    Sistema de envíos de tienda online 
    Puede enviar:
    . Mensajería estándar
    . Envío express
    . Envío internacional

    Cada uno se calcula de forma diferente
"""

class MetodoEnvio:
    def calcular_costo(self, peso):
        pass

class EnvioEstandar(MetodoEnvio):
    def calcular_costo(self, peso):
        return peso * 2000

class EnvioExpress(MetodoEnvio):
    def calcular_costo(self, peso):
        return peso * 5000

class EnvioInternacional(MetodoEnvio):
    def calcular_costo(self, peso):
        return peso * 10000

class EnvioDrone(MetodoEnvio):
    def calcular_costo(self, peso):
        return peso * 20000

    
class Pedido:
    def __init__(self, peso, metodo_envio: MetodoEnvio):
        self.peso = peso
        self.metodo_envio = metodo_envio
    
    def calcular_total_envio(self):
        return self.metodo_envio.calcular_costo(self.peso)

pedido1 = Pedido(10, EnvioEstandar())
pedido2 = Pedido(20, EnvioExpress())
pedido3 = Pedido(10, EnvioInternacional())
pedido4 = Pedido(10, EnvioDrone())


print(pedido1.calcular_total_envio())
print(pedido2.calcular_total_envio())
print(pedido3.calcular_total_envio())
print(pedido4.calcular_total_envio())