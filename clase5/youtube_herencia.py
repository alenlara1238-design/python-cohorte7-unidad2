class Video:
    def __init__(self, titulo, autor, duracion):
        self.titulo = titulo
        self.autor = autor
        self.duracion = duracion


class Short(Video):
        pass
        

class Largo(Video):
    def __init__(self, titulo, autor, duracion, likes):
        super().__init__(titulo, autor, duracion)
        self.likes = likes




short1 = Short("Aprendiendo Python", "Dev Senior", 25)