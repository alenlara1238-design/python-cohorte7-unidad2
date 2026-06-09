class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

persona = Persona("Carlos") #Instanciando

persona.__nombre = "Pedro" #Escribir o modificar el atributo
print(persona.__nombre) # Puedo acceder al atributo directamente? (Leerlo o escribir en él?)
