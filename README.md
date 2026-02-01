# Calculadora básica por consola en Python

Proyecto introductorio en Python que permite realizar operaciones matemáticas básicas
desde la consola.

# Funciones
- Suma, resta, multiplicación y división
- Manejo de errores al ingresar números
- Prevención de división por cero
- Bucle continuo hasta que el usuario decide salir

# Cómo usar el programa
1. Ejecutar el archivo `calculadora.py`
2. Ingresar los números solicitados
3. Elegir la operación (+, -, *, /)
4. Indicar si se desea continuar o salir

# Tecnologías utilizadas
- Python 3
- Consola

# Autora
Paleo Sol

## Funciones y Estructura usados en este proyecto:

### 1. `print()`
Muestra mensajes en la consola.

### 2. `input()`
Pide datos al usuario desde la consola.
⚠ Siempre devuelve un **string**.

### 3. `float()`
Convierte un texto (`str`) en un número decimal.
**En mi proyecto:**
* Convertir lo que escribe el usuario en números operables


### 4. `while True`
Crear un bucle que se repite indefinidamente hasta que se use `break`.
**En mi proyecto:**
* Permitir que el usuario haga **varias operaciones** sin reiniciar el programa

### 5. `if / elif / else`
Tomar decisiones según condiciones.
**En mi proyecto:**
* Elegir qué operación matemática realizar
* Detectar operaciones inválidas
* Controlar división por cero

### 6. `try / except ValueError`
Manejar errores que pueden ocurrir en tiempo de ejecución, sin que el programa se caiga.
**En mi proyecto:**
* Evitar que el programa se bloquee si el usuario ingresa letras en vez de números

### 7. `continue`
Salta directamente a la siguiente vuelta del bucle.
**En mi proyecto:**
* Volver a pedir datos si la operación es inválida, sin salir del programa

### 8. `break`
Salir definitivamente del bucle.
**En mi proyecto:**
* Terminar el programa cuando el usuario decide no continuar
  
### 9. `lower()`
Convierte un texto a minúsculas.
**En mi proyecto:**
* Acepta `"No"`, `"NO"`, `"no"` sin problemas

### 10. Operadores matemáticos
Realizar cálculos.
**usados en este proyecto:**
* `+` suma
* `-` resta
* `*` multiplicación
* `/` división
