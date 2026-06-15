# 🧩 Taller: Relaciones 1 a 1 entre Clases en Python

## Objetivos

Al finalizar este taller serás capaz de:

-   Identificar las clases necesarias a partir de un problema.
-   Descubrir cuándo un atributo debe ser un objeto.
-   Implementar una relación **1 a 1** entre clases.
-   Aplicar encapsulamiento utilizando **getters** y **setters**
    tradicionales.
-   Organizar un proyecto separando las clases en diferentes archivos.

> **Importante:** En este taller **NO** debes utilizar listas,
> colecciones, herencia, menús, ciclos (`for` o `while`) ni lectura de
> archivos. El objetivo es practicar únicamente las relaciones **1 a 1**
> entre clases.

------------------------------------------------------------------------

# Ejercicio 1 -- Plataforma de Música 🎵

## Contexto

Una plataforma de música permite reproducir canciones.

Cada **Canción** tiene un único **Artista** que la interpreta.

Del artista se desea conocer:

-   Nombre artístico
-   País
-   Número de seguidores
-   Si posee una cuenta verificada

De la canción se desea conocer:

-   Título
-   Duración
-   Número de reproducciones

## Parte 1. Análisis

Antes de escribir código, responde:

1.  ¿Cuántas clases necesita el sistema?
2.  ¿Cómo se llamará cada clase?
3.  ¿Qué atributos tendrá cada clase?
4.  ¿Cuál atributo de la clase `Cancion` debe almacenar un objeto?

------------------------------------------------------------------------

## Parte 2. Desarrollo

Implementa las clases necesarias.

Luego:

-   Crea un objeto `Artista`.
-   Crea un objeto `Cancion`.
-   Relaciona ambos objetos.

------------------------------------------------------------------------

## Parte 3. Navegación entre objetos

Imprime:

-   El título de la canción.
-   El nombre del artista.
-   El país del artista.
-   La cantidad de seguidores del artista.

Accede a la información utilizando el operador punto (`.`).

------------------------------------------------------------------------

## Parte 4. Encapsulamiento

El atributo **seguidores** del artista no puede ser negativo.

Realiza lo siguiente:

-   Encapsula el atributo.
-   Implementa un getter.
-   Implementa un setter con validación.
-   Prueba el setter con un valor válido.
-   Prueba el setter con un valor inválido.

------------------------------------------------------------------------

## Parte 5. Organización del proyecto

Organiza el proyecto utilizando la siguiente estructura:

``` text
musica/
│── artista.py
│── cancion.py
└── main.py
```

------------------------------------------------------------------------

# Ejercicio 2 -- Plataforma de Streaming 🎬

## Contexto

Una plataforma de streaming almacena información sobre películas.

Cada **Película** tiene un único **Director**.

Del director se conoce:

-   Nombre
-   Nacionalidad
-   Cantidad de premios obtenidos
-   Si continúa activo

De la película se conoce:

-   Título
-   Género
-   Duración

## Parte 1. Análisis

Antes de programar, responde:

1.  ¿Qué clases necesita el sistema?
2.  ¿Qué atributos tendrá cada clase?
3.  ¿Cuál atributo de la clase `Pelicula` debe almacenar un objeto?

------------------------------------------------------------------------

## Parte 2. Desarrollo

Implementa las clases necesarias.

Luego:

-   Crea un objeto `Director`.
-   Crea un objeto `Pelicula`.
-   Relaciona ambos objetos.

------------------------------------------------------------------------

## Parte 3. Navegación entre objetos

Imprime:

-   El título de la película.
-   El nombre del director.
-   La nacionalidad del director.
-   La cantidad de premios obtenidos por el director.

Utiliza el operador punto (`.`).

------------------------------------------------------------------------

## Parte 4. Encapsulamiento

La cantidad de premios obtenidos nunca puede ser negativa.

Realiza:

-   Encapsulamiento del atributo.
-   Getter.
-   Setter.
-   Validación correspondiente.
-   Prueba el setter con datos válidos e inválidos.

------------------------------------------------------------------------

## Parte 5. Organización del proyecto

Organiza el proyecto utilizando la siguiente estructura:

``` text
streaming/
│── director.py
│── pelicula.py
└── main.py
```

------------------------------------------------------------------------

# Criterios de evaluación

Se evaluará que el estudiante:

-   Identifique correctamente las clases.
-   Modele adecuadamente la relación **1 a 1**.
-   Cree e instancie correctamente los objetos.
-   Navegue entre objetos utilizando el operador punto (`.`).
-   Aplique encapsulamiento mediante getters y setters.
-   Organice el proyecto separando cada clase en su propio archivo.
