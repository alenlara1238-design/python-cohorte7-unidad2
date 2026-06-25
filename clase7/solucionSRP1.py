# Reponsabilidad: manejar el cálculo y los datos de una factura
class Factura:
    def __init__(self, cliente: str, total: float):
        self.cliente = cliente
        self.total = total
    
    def calcular_impuesto(self) -> float:
        # Calcula un impuesto fijo del 19%
        return self.total * 0.19
    
    def calcular_total_con_impuesto(self) -> float:
        return self.total + self.calcular_impuesto()


# Responsabilidad: Persistencia (guardar) de los datos
class FacturaRepositorio:
    def guardar(self, factura: Factura):
        print(f"[Almacenamiento] Factura de {factura.cliente} almacenada con éxito")
    

class ServicioNotificacion:
    def enviar_comprobante_email(self, factura: Factura):
        total_final = factura.calcular_total_con_impuesto()
        print(f"[Email] Notificación enviada a {factura.cliente}. Total con Iva {total_final}")


mi_factura = Factura("Alejandra", 10000)

almacenamiento = FacturaRepositorio()
notificador = ServicioNotificacion()

almacenamiento.guardar(mi_factura)
notificador.enviar_comprobante_email(mi_factura)