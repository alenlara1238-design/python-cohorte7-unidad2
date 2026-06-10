# Ejercicios de Programación Orientada a Objetos en Python

## Ejercicio 1: Sistema de Academia Online

### Situación Problema

La empresa **EducaTech** está desarrollando una plataforma de aprendizaje virtual donde los estudiantes pueden realizar cursos en línea.

Para ello, necesita representar a cada estudiante mediante una clase en Python.

De cada estudiante se desea almacenar la siguiente información:

- Nombre completo.
- Curso en el que está matriculado.
- Porcentaje de avance del curso.

La plataforma debe permitir que los estudiantes avancen en sus cursos a medida que completan actividades.

También debe permitir consultar la información de cada estudiante.

### Reglas del sistema

1. El porcentaje de avance nunca puede ser menor que 0.
2. El porcentaje de avance nunca puede ser mayor que 100.
3. El porcentaje de avance no debe modificarse directamente desde fuera de la clase.
4. Toda modificación del avance debe realizarse mediante métodos definidos en la clase.

### Actividad de Análisis

Antes de programar, responde:

1. ¿Cuál es la entidad principal del problema?
2. ¿Qué información debe almacenar esa entidad?
3. ¿Cuál de esos atributos debería protegerse mediante encapsulamiento?
4. ¿Qué acciones puede realizar esa entidad?
5. ¿Qué reglas de negocio deben cumplirse?

### Requerimientos de Programación

Diseña una clase que represente a un estudiante de la plataforma.

#### Constructor

Debe recibir:

- nombre
- curso
- avance

#### Encapsulamiento

El atributo **avance** debe estar encapsulado.

#### Getter

Crear un método que permita consultar el porcentaje de avance.

#### Setter

Crear un método que permita modificar el avance validando que siempre permanezca entre 0 y 100.

#### Método adicional

Crear un método que permita completar actividades y aumentar el avance del estudiante.

Si el resultado supera el 100%, el avance debe mantenerse en 100%.

#### Método de información

Crear un método que muestre toda la información del estudiante.

---

## Ejercicio 2: Control de Temperatura de un Aire Acondicionado

### Situación Problema

Una empresa fabricante de electrodomésticos está desarrollando el software para controlar un aire acondicionado inteligente.

Cada aire acondicionado debe almacenar:

- Marca.
- Modelo.
- Temperatura actual.

El usuario puede:

- Aumentar la temperatura.
- Disminuir la temperatura.
- Consultar la información del equipo.

Para evitar daños en el sistema, el fabricante ha definido las siguientes reglas.

### Reglas del sistema

1. La temperatura mínima permitida es 16°C.
2. La temperatura máxima permitida es 30°C.
3. La temperatura no debe modificarse directamente desde fuera de la clase.
4. Toda modificación debe realizarse mediante métodos.

### Actividad de Análisis

Antes de programar, responde:

1. ¿Cuál es la entidad principal del problema?
2. ¿Qué atributos tiene?
3. ¿Cuál atributo debería protegerse?
4. ¿Qué acciones puede realizar el aire acondicionado?
5. ¿Qué reglas deben cumplirse?

### Requerimientos de Programación

Diseña una clase que represente un aire acondicionado.

#### Constructor

Debe recibir:

- marca
- modelo
- temperatura

#### Encapsulamiento

El atributo **temperatura** debe estar encapsulado.

#### Getter

Crear un método que permita consultar la temperatura actual.

#### Setter

Crear un método que permita modificar la temperatura validando que permanezca entre 16°C y 30°C.

#### Métodos adicionales

Crear métodos que permitan:

- Aumentar la temperatura.
- Disminuir la temperatura.

Las reglas de temperatura mínima y máxima siempre deben respetarse.

#### Método de información

Crear un método que muestre toda la información del equipo.
