"""
    Tarjeta de crédito: comisión del 5%.
    Transferencia bancaria: No tiene comisión
    Billetera digital: descuento del 2%.
    Criptomoneda: recargo del 10%.

"""
#clase padre
class MetodoPago:

    def procesar_pago(self, valor):
        pass

class TarjetaCredito(MetodoPago):
    
    def procesar_pago(self, valor):
        comision = valor * 0.05
        return valor + comision

class TransferenciaBancaria(MetodoPago):

    def procesar_pago(self, valor):
        return valor

class BilleteraDigital(MetodoPago):

    def procesar_pago(self, valor):
        descuento = valor * 0.02
        return valor - descuento

class Criptomoneda(MetodoPago):

    def procesar_pago(self, valor):
        recargo = valor * 0.10
        return valor + recargo

class Contraentrega(MetodoPago):

    def procesar_pago(self, valor):
        return valor + 8000

# este e sel sistema que trabaja con las estrategias (el método polimórfico procesar_pago())
class Compra:
    def __init__(self, valor, metodo_pago: MetodoPago):
        self.valor = valor
        self.metodo_pago = metodo_pago
    
    def calcular_total(self):
        return self.metodo_pago.procesar_pago(self.valor)



compra1 = Compra(10000, TarjetaCredito())
compra2 = Compra(10000, Criptomoneda())
compra3 = Compra(10000, TransferenciaBancaria())
compra4 = Compra(10000, BilleteraDigital())
compra5 = Compra(10000, Contraentrega())

print("Tarjeta crédito:")
print(compra1.calcular_total())

print("----------------")

print("Criptommoneda")
print(compra2.calcular_total())


print("----------------")

print("Transferencia bancaria")
print(compra3.calcular_total())


print("----------------")

print("Billetera digital")

print(compra4.calcular_total())

print("----------------")

print("Contra entrega")

print(compra5.calcular_total())
