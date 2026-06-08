# Encapsulamiento en Python

## ¿Qué es el encapsulamiento?

El **encapsulamiento** es uno de los principios fundamentales de la
Programación Orientada a Objetos (POO). Consiste en **proteger los datos
de un objeto**, controlando la forma en que pueden ser consultados o
modificados.

En lugar de permitir que cualquier parte del programa cambie los
atributos libremente, la propia clase establece las reglas para acceder
a ellos. De esta forma, se evita que un objeto quede en un estado
inválido o inconsistente.

### Definición

> **El encapsulamiento es el principio que consiste en ocultar o
> proteger los datos internos de una clase y controlar su acceso
> mediante métodos definidos por la propia clase.**

Su objetivo principal es:

-   Proteger la integridad de los datos.
-   Evitar modificaciones incorrectas.
-   Facilitar el mantenimiento del código.
-   Hacer que las clases sean más seguras y reutilizables.

------------------------------------------------------------------------

## ¿Qué significa encapsular?

La palabra **encapsular** significa **encerrar o agrupar algo dentro de
una cápsula**.

En programación, encapsular significa:

-   Agrupar los **datos (atributos)** y los **comportamientos
    (métodos)** dentro de una misma clase.
-   Ocultar los detalles internos del objeto.
-   Permitir que otras partes del programa interactúen con el objeto
    únicamente mediante los mecanismos definidos por la clase.

### Ejemplo cotidiano

Pensemos en un cajero automático.

Como usuario podemos:

-   Consultar el saldo.
-   Retirar dinero.
-   Depositar dinero.

Sin embargo, **no podemos modificar directamente el saldo almacenado en
el sistema del banco**. Todas las operaciones pasan por reglas y
validaciones.

Del mismo modo, una clase encapsulada protege sus datos internos y solo
permite modificarlos mediante métodos controlados.

------------------------------------------------------------------------

# Atributos protegidos

En Python, un **atributo protegido** se identifica utilizando un **guion
bajo (`_`)** al inicio de su nombre.

``` python
class Persona:

    def __init__(self, nombre):
        self._nombre = nombre
```

El prefijo `_` **no impide el acceso** al atributo, sino que actúa como
una **convención** para indicar a otros programadores que dicho atributo
es de uso interno y no debería modificarse directamente desde fuera de
la clase.

## Ejemplo

``` python
persona = Persona("Carlos")

print(persona._nombre)
```

Aunque el código funciona, la recomendación es **no acceder ni modificar
directamente** un atributo protegido desde fuera de la clase.

## ¿Por qué usar atributos protegidos?

Los atributos protegidos permiten:

-   Comunicar que el atributo es interno.
-   Reducir modificaciones accidentales.
-   Facilitar el mantenimiento del código.
-   Preparar la clase para futuras validaciones.

## Diferencia entre atributo público y protegido

  Público                     Protegido
  --------------------------- --------------------------------------
  `self.nombre`               `self._nombre`
  Acceso libre                Acceso permitido, pero desaconsejado
  No comunica restricciones   Indica que es de uso interno

> **Importante:** En Python, un atributo protegido es una
> **convención**, no una restricción técnica. El lenguaje confía en que
> los desarrolladores respeten esta práctica para escribir código más
> claro y mantenible.
