class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base
    
    def calcular_pago(self):
        # este es el comportamiento por defecto
        return self.salario_base

class Desarrollador(Empleado):
    def __init__(self, nombre, salario_base, bono_proyecto):
        super().__init__(nombre, salario_base)
        self.bono_proyecto = bono_proyecto
    
    # Este método está sobreescrito en la clase hija
    def calcular_pago(self):
        return self.salario_base + self.bono_proyecto

class Gerente(Empleado):
    def __init__(self, nombre, salario_base, porcentaje_bono):
        super().__init__(nombre, salario_base)
        self.porcentaje_bono = porcentaje_bono
    
    def calcular_pago(self):
        return self.salario_base * (1 + self.porcentaje_bono)


class Disenador(Empleado):
    def __init__(self, nombre, salario_base, descuento_software):
        super().__init__(nombre, salario_base)
        self.descuento_software = descuento_software
    
    def calcular_pago(self):
        return self.salario_base - self.descuento_software




# Aqui somos usuarios de las clases y metodos

def imprimir_empleado(empleado):
    print(f"Empleado: {empleado.nombre} | Pago total: {empleado.calcular_pago():.2f}")


gerente = Gerente("Alejandro bustos", 45000, 0.1)
desarrollador = Desarrollador("Juan David", 5600, 1200)
disenador = Disenador("Alfredo Masa", 2000, 200)

imprimir_empleado(gerente) # 49.500
imprimir_empleado(desarrollador) # 6.800 = base + bono (desarrollador)
imprimir_empleado(disenador) 