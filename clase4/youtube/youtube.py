from autor import Autor
from video import Video

#================
# Progama Principal 
#================

#empezamos a instanciar objetos:
autor1 = Autor("Dev Senior", 2, "Colombia", True)
video1 = Video("Aprende python desde cero", "18:30", 125000, autor1)
print(video1.autor.nombre)
print(video1.autor.pais)

video1.autor.nombre = "Dev Senior Code LLC"

#video1.autor.__suscriptores = 3555
video1.autor.set_suscriptores(-3555)
autor1.mostrar_info()
#video1.mostrar_info()