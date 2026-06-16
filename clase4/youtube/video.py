from autor import Autor #Indica que esta clase necesita la clase Autor
# La clase autor es dependencia de la clase Video

class Video:

    def __init__(self, titulo, duracion, visualizaciones, autor):
        self.titulo = titulo
        self.duracion = duracion
        self.visualizaciones = visualizaciones
        # Aquí alamcenamos un objeto autor
        self.autor = autor
    
    def mostrar_info(self):
        print("\n===Video====")
        print(f"Titulo: {self.titulo}")
        print(f"Duración: {self.duracion}")
        print(f"Visualizaciones: {self.visualizaciones}")
        self.autor.mostrar_info()

