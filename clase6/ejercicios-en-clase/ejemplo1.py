# clase padre
class Contenido:
    def reproducir(self):
        pass

# clases hijas
class Video(Contenido):
    def reproducir(self):
        print("Reproduciendo video")


class Short(Contenido):
    def reproducir(self):
        print("Reproduciendo short")

class Podcast(Contenido):
    def reproducir(self):
        print("Reproduciendo podcast")

class Publicidad(Contenido):
    def reproducir(self):
        print("reproduciendo publicidad")

class ContenidoX:
    pass


# Significa que diferentes objetos pueden responder al mismo mensaje de maneras distintas.

def reproductor(contenido: Contenido):
    contenido.reproducir()



reproductor(Video())
reproductor(Short())
reproductor(Publicidad())

# El polimorfismo es una consecuencia de la herencia.