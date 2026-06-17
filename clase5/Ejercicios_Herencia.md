# Ejercicios Progresivos - Clase 5: Herencia en Python

La siguiente secuencia de ejercicios está diseñada siguiendo una
progresión didáctica. Cada ejercicio introduce un único concepto nuevo
para que el estudiante construya el conocimiento paso a paso, evitando
añadir complejidad innecesaria.

------------------------------------------------------------------------

# Ejercicio 1. Mi primera herencia

## Objetivo

Crear la primera relación de herencia entre una clase padre y una clase
hija.

## Enunciado

Una empresa desea registrar diferentes tipos de personas.

Toda persona posee información básica que también tendrán los empleados.

### Paso 1

Cree una clase llamada **Persona**.

Debe almacenar: - nombre - edad

### Paso 2

Dentro de la clase **Persona**, cree un método llamado `presentarse()`
que muestre el nombre y la edad de la persona.

### Paso 3

Cree una clase llamada **Empleado** que herede de **Persona**.

Por ahora **no agregue ningún atributo ni método nuevo**.

### Paso 4

Cree un objeto de la clase **Empleado** utilizando el constructor
heredado.

### Paso 5

Compruebe que el objeto puede: - acceder al atributo `nombre` - acceder
al atributo `edad` - ejecutar el método `presentarse()`

### Preguntas de reflexión

1.  ¿La clase Empleado tiene constructor propio?
2.  ¿De dónde obtiene el método `presentarse()`?
3.  ¿Fue necesario volver a escribir ese método?

------------------------------------------------------------------------

# Ejercicio 2. Agregando un nuevo atributo

## Objetivo

Aprender a reutilizar el constructor del padre utilizando `super()`.

## Enunciado

Una tienda vende diferentes dispositivos electrónicos.

### Paso 1

Cree la clase **Dispositivo** con los atributos: - marca - modelo

### Paso 2

Agregue el método `mostrar_informacion()` que imprima la marca y el
modelo.

### Paso 3

Cree la clase **Celular** que herede de **Dispositivo**.

### Paso 4

Agregue un atributo exclusivo: - almacenamiento

### Paso 5

Utilice `super()` para inicializar los atributos heredados.

### Paso 6

Cree un objeto y muestre: - marca - modelo - almacenamiento

Finalmente ejecute el método heredado.

### Preguntas de reflexión

-   ¿Qué ocurriría si no se llamara a `super()`?
-   ¿Qué atributos pertenecen al padre?
-   ¿Cuál pertenece únicamente al hijo?

------------------------------------------------------------------------

# Ejercicio 3. Dos clases hijas

## Objetivo

Comprender que una misma clase padre puede tener varias clases hijas.

## Enunciado

Una empresa fabrica diferentes tipos de muebles.

### Paso 1

Diseñe la clase **Mueble**.

Atributos: - material - color

Método: - `describir()`

### Paso 2

Cree la clase **Mesa** agregando: - cantidad_patas

### Paso 3

Cree la clase **Silla** agregando: - tiene_espaldar

### Paso 4

Utilice `super()` en ambas clases.

### Paso 5

Cree un objeto de cada tipo y verifique que ambos puedan utilizar el
método heredado.

Complete antes el siguiente esquema:

``` text
               Mueble
              ___________

             /           \
            /             \

        _________      _________
```

------------------------------------------------------------------------

# Ejercicio 4. Identificando la clase padre

## Objetivo

Aprender a identificar correctamente qué información debe pertenecer a
la clase padre.

## Enunciado

En un zoológico existen: - Leones - Elefantes

Todos poseen: - nombre - peso

Además:

El león tiene: - cantidad de miembros en la manada

El elefante tiene: - longitud de la trompa

### Actividad 1

Complete la tabla:

  Información                         ¿Padre o hijo?
  ----------------------------------- ----------------
  nombre                              
  peso                                
  cantidad de miembros en la manada   
  longitud de la trompa               

### Actividad 2

Escriba cuál será la clase padre.

### Actividad 3

Escriba cuáles serán las clases hijas.

### Actividad 4

Implemente la solución en Python.

------------------------------------------------------------------------

# Ejercicio 5. Construyendo una jerarquía completa

## Objetivo

Aplicar todo lo aprendido sobre herencia.

## Enunciado

Una universidad desea organizar la información de las personas que hacen
parte de la institución.

Existen dos tipos: - Docentes - Estudiantes

Toda persona posee: - nombre - documento

Además: - El docente posee: profesión. - El estudiante posee: semestre.

### Paso 1

Complete el siguiente diseño antes de programar.

``` text
                 _____________
                |             |
                |             |
                |_____________|
                       ▲
             __________|___________
            |                      |
            |                      |
     _________________      _________________
    |                 |    |                 |
    |                 |    |                 |
    |_________________|    |_________________|
```

### Paso 2

Cree la clase padre.

### Paso 3

Agregue un método que muestre la información básica.

### Paso 4

Cree ambas clases hijas utilizando `super()`.

### Paso 5

Instancie un objeto de cada clase.

### Paso 6

Verifique que ambos puedan utilizar el método heredado.

### Reflexión

-   ¿Qué ventajas obtuvo al utilizar herencia?
-   ¿Qué código no tuvo que repetir?

------------------------------------------------------------------------

# Ejercicio 6. Reto Integrador

## Objetivo

Diseñar una jerarquía de clases a partir de un problema sin indicar
explícitamente las clases.

## Enunciado

Una empresa desarrolla un sistema para administrar vehículos de
emergencia.

En el sistema se registrarán: - Ambulancias - Camiones de bomberos

### Su tarea consiste en:

1.  Analizar el problema.
2.  Determinar la clase padre y las clases hijas.
3.  Identificar los atributos comunes.
4.  Identificar los atributos exclusivos de cada clase hija.
5.  Crear un método común para todos los vehículos.
6.  Implementar toda la jerarquía utilizando herencia.
7.  Crear un objeto de cada tipo y comprobar que ambos reutilizan
    correctamente los atributos y métodos heredados.

------------------------------------------------------------------------

# Desafío Final (Opcional)

Elija uno de los siguientes contextos:

-   Instrumentos musicales.
-   Electrodomésticos.
-   Animales domésticos.
-   Equipos deportivos.
-   Productos de una tienda.
-   Empleados de un hospital.
-   Figuras geométricas.
-   Medios de transporte.
-   Dispositivos tecnológicos.
-   Libros de una biblioteca.

Antes de escribir el código complete la siguiente plantilla:

  Elemento                            Respuesta
  ----------------------------------- -----------
  Clase padre                         
  Clase hija 1                        
  Clase hija 2                        
  Atributos comunes                   
  Atributos exclusivos de la hija 1   
  Atributos exclusivos de la hija 2   
  Método heredado                     
