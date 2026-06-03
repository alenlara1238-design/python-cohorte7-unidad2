# Clase 1: Introducción a la Programación Orientada a Objetos (POO) en Python

## ¿Qué es la Programación Orientada a Objetos?

La Programación Orientada a Objetos (POO) es un paradigma de programación que organiza los programas alrededor de **objetos**.

Un objeto combina:

- Datos (información)
- Comportamientos (acciones)

### Ejemplo del mundo real

Un perro tiene:

**Características**
- Nombre
- Edad
- Raza

**Comportamientos**
- Ladrar
- Comer
- Correr

La POO intenta representar este tipo de elementos dentro de nuestros programas.

---

# Programación Estructurada vs Programación Orientada a Objetos

## Programación Estructurada

La información suele almacenarse en variables separadas.

```python
nombre = "Firulais"
edad = 5
raza = "Labrador"
```

Si tenemos muchos perros, necesitaremos muchas variables.

```python
nombre1 = "Firulais"
edad1 = 5

nombre2 = "Max"
edad2 = 3

nombre3 = "Rocky"
edad3 = 7
```

Esto puede volverse difícil de mantener.

---

## Programación Orientada a Objetos

La información relacionada se agrupa dentro de objetos.

```python
perro = Perro("Firulais", 5)
```

Todo lo relacionado con el perro queda organizado en una sola estructura.

---

# Concepto 1: Clase

Una clase es una plantilla o molde para crear objetos.

### Analogía

Una clase es como el plano de una casa.

El plano describe cómo será la casa, pero todavía no existe una casa real.

### Ejemplo

```python
class Perro:
    pass
```

Aquí hemos definido una clase llamada `Perro`.

---

# Concepto 2: Objeto

Un objeto es una instancia creada a partir de una clase.

### Analogía

Si la clase es el plano, el objeto es la casa construida.

### Ejemplo

```python
class Perro:
    pass

firulais = Perro()
```

`firulais` es un objeto creado a partir de la clase `Perro`.

---

# Concepto 3: Atributo

Los atributos representan las características de un objeto.

### Analogía

Las características de una persona:

- Nombre
- Edad
- Estatura

### Ejemplo

```python
class Perro:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
```

Los atributos son:

```python
self.nombre
self.edad
```

---

# Concepto 4: Método

Un método representa una acción que puede realizar un objeto.

### Analogía

Un perro puede:

- Ladrar
- Correr
- Comer

Estas acciones pueden representarse mediante métodos.

### Ejemplo

```python
class Perro:

    def ladrar(self):
        print("Guau")
```

Uso:

```python
perro = Perro()
perro.ladrar()
```

Salida:

```text
Guau
```

---
# Concepto 5: Constructor init
El constructor es un método especial que se ejecuta automáticamente cuando se crea un objeto.

Su función principal es inicializar los atributos.

### Ejemplo

```python
class Perro:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
```

Crear objetos:

```python
perro1 = Perro("Firulais", 5)
perro2 = Perro("Max", 3)
```

Cada objeto tendrá sus propios datos.

---

# Concepto 6: self

`self` representa al objeto actual.

Permite acceder a los atributos y métodos pertenecientes al objeto.

### Ejemplo

```python
class Perro:

    def __init__(self, nombre):
        self.nombre = nombre

    def presentarse(self):
        print("Hola, soy", self.nombre)
```

Uso:

```python
perro = Perro("Firulais")
perro.presentarse()
```

Salida:

```text
Hola, soy Firulais
```

---

# Relación entre Objetos y Comportamiento

Los objetos almacenan información y también pueden realizar acciones.

```python
class Videojuego:

    def __init__(self, nombre, vidas):
        self.nombre = nombre
        self.vidas = vidas

    def mostrar_estado(self):
        print(self.nombre)
        print("Vidas:", self.vidas)
```

Uso:

```python
juego = Videojuego("Super Python", 3)
juego.mostrar_estado()
```

Salida:

```text
Super Python
Vidas: 3
```

---

# Ejemplo Completo

```python
class Estudiante:

    def __init__(self, nombre, curso):
        self.nombre = nombre
        self.curso = curso

    def presentarse(self):
        print("Hola, soy", self.nombre)
        print("Curso:", self.curso)


ana = Estudiante("Ana", "Python")

ana.presentarse()
```

Salida:

```text
Hola, soy Ana
Curso: Python
```

---

# Resumen de Conceptos

| Concepto | Descripción | Analogía |
|-----------|-----------|-----------|
| Clase | Molde para crear objetos | Plano de una casa |
| Objeto | Instancia creada desde una clase | Casa construida |
| Atributo | Característica del objeto | Nombre, edad |
| Método | Acción del objeto | Ladrar, correr |
| Constructor | Inicializa atributos | Preparar una casa antes de habitarla |
| self | Referencia al objeto actual | "Yo mismo" dentro del objeto |

---

# Objetivo Alcanzado

Al finalizar esta clase el estudiante debe ser capaz de:

- Explicar qué es la Programación Orientada a Objetos.
- Diferenciar programación estructurada y orientada a objetos.
- Crear clases sencillas en Python.
- Instanciar objetos.
- Definir atributos y métodos básicos.
- Comprender la relación entre objetos, información y comportamiento.
