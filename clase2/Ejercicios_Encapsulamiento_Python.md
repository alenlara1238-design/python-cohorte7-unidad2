# Ejercicios de Encapsulamiento en Python

## Ejercicio 1 - Cuenta Bancaria (Muy fácil)

```python
class CuentaBancaria:

    """
    Atributos:
    - Titular: obligatorio
    - Saldo: nunca puede ser negativo (sensible)

    Tarea:
    1. Crear el constructor.
    2. Encapsular el saldo.
    3. Crear get_saldo().
    4. Crear set_saldo().
    5. Solo permitir valores mayores o iguales a cero.
    """

    def __init__(self, titular, saldo):
        # completar

    # get_saldo

    # set_saldo
```

## Ejercicio 2 - Estudiante

```python
class Estudiante:

    """
    Atributos:
    - Nombre
    - Edad (entre 5 y 100 años)
    - Promedio (entre 0 y 5)

    Edad y promedio son sensibles.

    Tarea:
    - Crear constructor.
    - Crear getters.
    - Crear setters.
    - Validar los rangos.
    """

    def __init__(self, nombre, edad, promedio):
        pass

    # getters

    # setters
```

## Ejercicio 3 - Vehículo

```python
class Vehiculo:

    """
    Atributos:
    - Marca
    - Modelo
    - Velocidad (0 - 220 km/h)
    - Combustible (0 - 100 litros)

    Validaciones:
    0 <= velocidad <= 220
    0 <= combustible <= 100
    """

    def __init__(self, marca, modelo, velocidad, combustible):
        pass
```

## Ejercicio 4 - Empleado

```python
class Empleado:

    """
    Atributos:
    - Nombre
    - Salario (> 0)
    - Horas trabajadas (0 - 240)
    """

    def __init__(self, nombre, salario, horas):
        pass
```

## Ejercicio 5 - Videojuego

```python
class Videojuego:

    """
    Atributos:
    - Título
    - Precio (> 0)
    - Clasificación PEGI (3, 7, 12, 16, 18)
    """

    def __init__(self, titulo, precio, clasificacion):
        pass
```

## Ejercicio 6 - ReservaHotel

```python
class ReservaHotel:

    """
    Atributos:
    - Cliente
    - Huéspedes (1 - 6)
    - Noches (1 - 30)
    """

    def __init__(self, cliente, huespedes, noches):
        pass
```

## Ejercicio 7 - Producto (Nivel intermedio)

```python
class Producto:

    """
    Atributos:
    - Nombre
    - Precio (> 0)
    - Stock (>= 0)
    - Descuento (0 - 50%)
    """

    def __init__(self, nombre, precio, stock, descuento):
        pass
```

## Ejercicio 8 - Curso

```python
class Curso:

    """
    Atributos:
    - Nombre
    - Cupos disponibles (0 - 40)
    - Duración en horas (1 - 300)
    - Costo (> 0)
    """

    def __init__(self, nombre, cupos, horas, costo):
        pass
```

## Ejercicio 9 - Tarjeta de Regalo (Nivel intermedio)

```python
class TarjetaRegalo:

    """
    Atributos:
    - Código
    - Saldo (>= 0)
    - Estado (ACTIVA o BLOQUEADA)
    """

    def __init__(self, codigo, saldo, estado):
        pass
```

## Ejercicio 10 - Celular (Nivel intermedio)

```python
class Celular:

    """
    Atributos:
    - Marca
    - Modelo
    - Batería (0 - 100)
    - Volumen (0 - 100)
    """

    def __init__(self, marca, modelo, bateria, volumen):
        pass
```

## Ejercicio 11 - Biblioteca (Nivel avanzado)

```python
class Libro:

    """
    Atributos:
    - Título
    - Autor
    - Número de páginas (> 0)
    - Ejemplares disponibles (>= 0)
    """

    def __init__(self, titulo, autor, paginas, ejemplares):
        pass
```

## Ejercicio 12 - Vuelo (Nivel avanzado)

```python
class Vuelo:

    """
    Atributos:
    - Código
    - Capacidad (1 - 300)
    - Pasajeros registrados (0 - capacidad)

    Regla:
    Nunca puede haber más pasajeros que la capacidad.
    """

    def __init__(self, codigo, capacidad, pasajeros):
        pass
```
