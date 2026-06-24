# Enunciado del Ejercicio: El Sistema de Facturación Express

## Contexto del problema

Estás trabajando en el sistema de una tienda en línea. Actualmente, un
desarrollador junior escribió una sola clase llamada `Factura` para
gestionar todo el proceso de venta de un cliente.

El código actual funciona, pero el dueño de la tienda quiere hacer
cambios en el futuro: quiere poder guardar las facturas en un archivo de
texto en lugar de solo imprimirlas en pantalla, y además quiere cambiar
el diseño del correo electrónico que se le envía al cliente.

Con el código actual, cualquier cambio obliga a modificar la clase
`Factura` por completo, lo que está generando errores en el sistema.

## El Código "Monolítico" Actual (A refactorizar)


``` python
class Factura:
    def __init__(self, cliente: str, total: float):
        self.cliente = cliente
        self.total = total

    def calcular_impuesto(self) -> float:
        # Calcula un impuesto fijo del 19%
        return self.total * 0.19

    def guardar_factura_en_sistema(self):
        # Simula guardar los datos en el sistema de almacenamiento
        print(f"Guardando en el sistema la factura de {self.cliente} por un total de ${self.total}")

    def enviar_comprobante_email(self):
        # Simula el envío de la notificación al cliente
        print(f"Enviando correo a {self.cliente}: 'Gracias por tu compra. Total pagado: ${self.total + self.calcular_impuesto()}'")
```

## Misión del Estudiante

Aplica el Principio de Responsabilidad Única (SRP) para dividir esta
clase "Navaja Suiza" en tres clases independientes, donde cada una tenga
un único motivo para cambiar.

Identifica las 3 responsabilidades ocultas en la clase original:

1.  ¿Quién debe conocer los datos de la venta y calcular sus montos?
2.  ¿Quién debe encargarse de almacenar/guardar la información?
3.  ¿Quién debe encargarse de la comunicación/notificación con el
    cliente?

Escribe el nuevo código en Python creando las tres clases separadas.

------------------------------------------------------------------------

# El Sistema de Combate de "Python Quest"

## Contexto del problema

Estás desarrollando un videojuego RPG en Python. Tu compañero de equipo
programó la clase `Personaje`, la cual representa al héroe del juego. El
código funciona para un combate simple, pero el diseñador del juego
quiere añadir nuevas mecánicas:

-   Quiere que cuando el personaje suba de nivel, el juego reproduzca un
    sonido épico de victoria.
-   Quiere cambiar la fórmula del daño para que dependa de si el arma
    está rota o no.
-   Quiere que el historial de la batalla no se imprima solo en la
    consola, sino que se guarde en un archivo de texto (`log.txt`) para
    analizar trampas.

Con el código actual, cualquier cambio en los sonidos, en el sistema de
archivos o en las reglas de daño obliga a romper la clase `Personaje`,
lo que está llenando el videojuego de bugs.

## El Código "Navaja Suiza" Actual (A refactorizar)


``` python
class Personaje:
    def __init__(self, nombre: str, fuerza: int, salud: int):
        self.nombre = nombre
        self.fuerza = fuerza
        self.salud = salud
        self.nivel = 1

    def atacar(self, enemigo_nombre: str):
        # 1. Lógica de cálculo de daño (Mecánica de juego)
        dano_infligido = self.fuerza * 2
        print(f"{self.nombre} ataca a {enemigo_nombre} e inflige {dano_infligido} de daño.")

    def subir_de_nivel(self):
        # 2. Lógica de progresión
        self.nivel += 1
        self.fuerza += 5
        print(f"{self.nombre} ha subido al nivel {self.nivel}. Sus músculos crecen.")

        # 3. Lógica de efectos de sonido (Multimedia)
        print("[Audio] Sonando: 'FANFARRIA_VICTORIA.MP3' a volumen 100%")

    def guardar_partida(self):
        # 4. Lógica de persistencia (Guardado en disco)
        print(f"[Archivo] Guardando progreso de {self.nombre} (Nivel {self.nivel}) en la ranura de guardado...")
```

## Misión del Estudiante

Aplica el Principio de Responsabilidad Única (SRP) para liberar al
`Personaje` de las tareas que no le corresponden. Debes dividir este
bloque en cuatro clases independientes:

Identifica las responsabilidades:

1.  ¿Quién debe contener solo los atributos del héroe y su estado
    físico?
2.  ¿Quién debe encargarse de calcular el daño y los efectos del
    combate?
3.  ¿Quién debe manejar el sistema de audio/sonido del juego?
4.  ¿Quién debe gestionar el guardado de la partida (guardar en disco)?

Escribe el código refactorizado en Python.
