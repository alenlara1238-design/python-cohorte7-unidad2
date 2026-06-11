# Ejercicios Guiados de Programación Orientada a Objetos en Python

## Ejercicio Guiado 1: Videojuego de Energía

### Situación Problema

Una empresa de videojuegos está desarrollando un personaje que puede realizar misiones.

Cada personaje tiene:
- Nombre
- Tipo de personaje
- Nivel de energía

### Reglas
- La energía no puede ser menor que 0.
- La energía no puede ser mayor que 100.
- La energía debe estar protegida mediante encapsulamiento.

### Paso 1: Analizar el problema
- ¿Cuál es la entidad principal?
- ¿Qué información necesita almacenar?
- ¿Cuál atributo debe encapsularse?

### Paso 2: Crear la clase
Crear una clase llamada Personaje.

### Paso 3: Crear el constructor
Debe recibir:
- nombre
- tipo
- energia

### Paso 4: Crear el Getter
Crear get_energia().

### Paso 5: Crear el Setter
Crear set_energia() validando que la energía permanezca entre 0 y 100.

### Paso 6: Crear un método de comportamiento
Crear realizar_mision().

### Paso 7: Crear otro método
Crear descansar().

### Paso 8: Mostrar información
Crear mostrar_info().

### Paso 9: Crear el Main
1. Crear un personaje.
2. Mostrar información.
3. Realizar una misión.
4. Consultar energía con el getter.
5. Descansar.
6. Intentar asignar una energía inválida.
7. Mostrar información nuevamente.

---

## Ejercicio Guiado 2: Sistema de Batería de un Smartphone

### Situación Problema

Una empresa fabricante de teléfonos celulares está desarrollando un simulador de batería.

Cada teléfono debe almacenar:
- Marca
- Modelo
- Porcentaje de batería

### Reglas
- La batería debe permanecer entre 0 y 100.
- La batería debe estar encapsulada.

### Paso 1: Analizar
- ¿Cuál es la entidad?
- ¿Qué atributos tiene?
- ¿Cuál atributo debe protegerse?

### Paso 2: Crear la clase
Crear Smartphone.

### Paso 3: Constructor
Debe recibir:
- marca
- modelo
- bateria

### Paso 4: Getter
Crear get_bateria().

### Paso 5: Setter
Crear set_bateria() validando valores entre 0 y 100.

### Paso 6: Método de descarga
Crear usar_aplicacion().

### Paso 7: Método de carga
Crear cargar().

### Paso 8: Método informativo
Crear mostrar_info().

### Paso 9: Main
1. Crear un teléfono.
2. Mostrar información.
3. Usar aplicaciones.
4. Consultar batería.
5. Cargar batería.
6. Intentar asignar un valor inválido.
7. Mostrar estado final.

---

## Ejercicio Guiado 3: Control de Agua de una Planta

### Situación Problema

Una aplicación de jardinería permite monitorear el nivel de agua de una planta.

Cada planta tiene:
- Nombre
- Tipo
- Nivel de agua

### Reglas
- El nivel de agua debe permanecer entre 0 y 100.
- El nivel de agua debe estar encapsulado.

### Paso 1: Identificar la entidad

### Paso 2: Identificar atributos

### Paso 3: Constructor

### Paso 4: Getter
Crear get_nivel_agua().

### Paso 5: Setter
Crear set_nivel_agua().

### Paso 6: Método de riego
Crear regar().

### Paso 7: Método de consumo
Crear pasar_dia().

### Paso 8: Método de información
Crear mostrar_info().

### Paso 9: Main
1. Crear una planta.
2. Regarla.
3. Simular varios días.
4. Consultar el nivel mediante el getter.
5. Intentar asignar un valor inválido.
6. Mostrar el estado final.
