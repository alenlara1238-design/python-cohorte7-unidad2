# Ejercicio: Sistema de pagos de una tienda online

## Contexto del problema

Una tienda online necesita implementar un sistema de pagos.

Actualmente existen diferentes formas en las que un cliente puede pagar:

-   Pago con tarjeta de crédito
-   Pago con transferencia bancaria
-   Pago con billetera digital
-   Pago con criptomonedas

Cada método de pago tiene una forma diferente de calcular el valor final
porque algunos tienen comisión.

El sistema de compra no debe saber cómo funciona cada pago, solamente
debe pedirle al método de pago que procese la operación.

La solución debe usar polimorfismo.

------------------------------------------------------------------------

# Requerimientos

## Crear una clase padre llamada:

`MetodoPago`

Debe tener un método:

``` python
procesar_pago(self, valor)
```

Este método será sobrescrito por cada forma de pago.

------------------------------------------------------------------------

# Crear las clases hijas

## TarjetaCredito

Calcula una comisión del 5%.

Ejemplo:

Compra:

    100000

Comisión:

    5000

Total:

    105000

------------------------------------------------------------------------

## TransferenciaBancaria

No tiene comisión.

Ejemplo:

Compra:

    100000

Resultado:

    100000

------------------------------------------------------------------------

## BilleteraDigital

Tiene un descuento del 2%.

Ejemplo:

Compra:

    100000

Descuento:

    2000

Total:

    98000

------------------------------------------------------------------------

## Criptomoneda

Tiene un recargo del 10%.

Ejemplo:

Compra:

    100000

Resultado:

    110000

------------------------------------------------------------------------

# Clase Compra

Crear una clase llamada:

`Compra`

Debe recibir:

-   Valor de la compra
-   Método de pago

Ejemplo:

``` python
compra = Compra(100000, TarjetaCredito())
```

La clase debe tener:

``` python
calcular_total()
```

Este método debe usar polimorfismo para llamar:

``` python
metodo_pago.procesar_pago()
```
