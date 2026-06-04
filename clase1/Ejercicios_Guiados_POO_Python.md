# Ejercicios Guiados de Programación Orientada a Objetos en Python

## Ejercicio 1: Sistema de Biblioteca

### Contexto

Una biblioteca necesita registrar los libros disponibles para préstamo.

### Tu misión

Crea una clase llamada `Libro`.

#### Atributos

- titulo
- autor
- cantidad_paginas

#### Método

```python
mostrar_informacion()
```

Este método debe mostrar todos los datos del libro.

#### Instanciación requerida

Debes crear dos objetos:

- Un libro de "Cien años de soledad"
- Un libro de "El Principito"

Luego llama al método para mostrar la información de ambos libros.

### Guía

**Paso 1**

Define la clase.

```python
class Libro:
```
**Paso 2**

Crea el constructor que reciba los atributos.

**Pregunta de reflexión**

¿Cuáles de los datos anteriores deben llegar como parámetros al constructor?

**Paso 3**

Guarda los valores utilizando `self`.

**Paso 4**

Implementa el método:

```python
mostrar_informacion()
```

**Paso 5**

Instancia dos objetos.

### Salida esperada

```text
Título: Cien años de soledad
Autor: Gabriel García Márquez
Páginas: 417

Título: El Principito
Autor: Antoine de Saint-Exupéry
Páginas: 96
```

---

## Ejercicio 2: Gestión de Vehículos

### Contexto

Una empresa de alquiler de vehículos necesita registrar los automóviles disponibles.

### Tu misión

Crea una clase llamada `Vehiculo`.

#### Atributos

- marca
- modelo
- color

#### Método

```python
encender()
```

El método debe indicar que el vehículo ha sido encendido.

#### Instanciación requerida

Crear:

- Un Toyota Corolla blanco
- Un Mazda CX-5 rojo

Posteriormente llamar al método `encender()`.

### Guía

**Paso 1**

Define la clase.

**Paso 2**

Construye el método constructor.

**Pregunta de reflexión**

¿Qué atributos pertenecen a cada vehículo individual?

**Paso 3**

Implementa el método:

```python
encender()
```

**Paso 4**

Crea dos objetos.

### Salida esperada

```text
El vehículo Toyota Corolla ha sido encendido.

El vehículo Mazda CX-5 ha sido encendido.
```

---

## Ejercicio 3: Plataforma de Streaming

### Contexto

Una plataforma de películas necesita registrar las producciones disponibles.

### Tu misión

Crea una clase llamada `Pelicula`.

#### Atributos

- nombre
- genero
- duracion

#### Método

```python
reproducir()
```

Debe indicar que la película está iniciando.

#### Instanciación requerida

Crear dos películas y reproducirlas.

### Guía

**Pregunta inicial**

Si cada película tiene características diferentes, ¿dónde deberían almacenarse esos datos?

**Paso 1**

Crear la clase.

**Paso 2**

Agregar el constructor.

**Paso 3**

Agregar el método `reproducir()`.

**Paso 4**

Crear dos objetos.

### Salida esperada

```text
Reproduciendo película: Interestelar

Reproduciendo película: Coco
```

---

## Ejercicio 4: Sistema de Pedidos

### Contexto

Un restaurante desea registrar pedidos realizados por sus clientes.

### Tu misión

Crear una clase llamada `Pedido`.

#### Atributos

- cliente
- producto
- precio

#### Método

```python
mostrar_resumen()
```

Debe mostrar un resumen del pedido.

#### Instanciación requerida

Crear dos pedidos diferentes.

### Guía

**Pregunta de análisis**

¿Qué información cambia entre un pedido y otro?

**Paso 1**

Definir la clase.

**Paso 2**

Implementar el constructor.

**Paso 3**

Crear el método solicitado.

**Paso 4**

Instanciar dos objetos.

### Salida esperada

```text
Cliente: Carlos
Producto: Hamburguesa
Precio: 25000

Cliente: Laura
Producto: Pizza
Precio: 38000
```

---

## Ejercicio 5: Gestión de Estudiantes

### Contexto

Una institución educativa necesita registrar estudiantes matriculados.

### Tu misión

Crear una clase llamada `Estudiante`.

#### Atributos

- nombre
- programa
- semestre

#### Método

```python
presentarse()
```

Debe mostrar una presentación del estudiante.

#### Instanciación requerida

Crear dos estudiantes.

### Guía

**Pregunta de reflexión**

¿Cada estudiante comparte los mismos valores de atributos o cada uno tiene información diferente?

**Paso 1**

Crear la clase.

**Paso 2**

Implementar el constructor.

**Paso 3**

Crear el método `presentarse()`.

**Paso 4**

Instanciar los objetos.

### Salida esperada

```text
Hola, soy Juan.
Estudio Ingeniería de Sistemas.
Estoy en semestre 4.

Hola, soy Ana.
Estudio Diseño Gráfico.
Estoy en semestre 2.
```

---

# Desafío Adicional

Completa las siguientes clases sin guía adicional.

| Clase | Atributos | Método |
|---------|---------|---------|
| Mascota | nombre, especie, edad | saludar() |
| CuentaBancaria | titular, saldo, numero | consultar_saldo() |
| Videojuego | nombre, categoria, precio | iniciar() |
| Producto | nombre, precio, stock | mostrar_detalle() |
| Curso | nombre, instructor, duracion | describir() |

Objetivo: demostrar el dominio de la relación entre clase, atributos, constructor, métodos, objetos e invocación de métodos.
