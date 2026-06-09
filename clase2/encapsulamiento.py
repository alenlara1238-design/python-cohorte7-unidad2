class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, nuevo_saldo):
        if nuevo_saldo >= 0:
            self.__saldo += nuevo_saldo
        else:
            self.__saldo = 0
            print("Error: saldo inválido")

cuenta1 = Cuenta("Ana", 1000) # Aqui instanciamos una cuenta
print(f"Leyendo saldo de cuenta perteneciente a {cuenta1.titular}: {cuenta1.get_saldo()}")
cuenta1.set_saldo(-10000)
print(f"Estableciendo valor nuevo a saldo: {cuenta1.get_saldo()}")

