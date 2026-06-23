# clase padre
class Personaje:
    def atacar(self):
        pass

# clases hijas
class Guerrero(Personaje):
    def atacar(self):
        print("Golpea con espada")
    
class Soldado(Personaje):
    def atacar(self):
        print("Dispara rafaga")

class Mago(Personaje):
    def atacar(self):
        print("Lanza hechizo")

#controlador del juego
def iniciar_ataque(personaje: Personaje):
    personaje.atacar()

iniciar_ataque(Guerrero())
iniciar_ataque(Mago())
iniciar_ataque(Soldado())
