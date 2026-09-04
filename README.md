# Memorama en Python

Proyecto académico individual desarrollado en Python que implementa un juego de memoria por consola sobre un tablero de 10 × 10.

El programa genera 50 pares de emojis, los distribuye aleatoriamente y permite al usuario seleccionar cartas mediante coordenadas hasta encontrar todos los pares.

## Funcionalidades

- Generación aleatoria de un tablero de 100 cartas.
- 50 pares de emojis.
- Selección de cartas mediante fila y columna.
- Validación de coordenadas ingresadas por el usuario.
- Detección de cartas ya descubiertas.
- Comparación de pares.
- Conteo de intentos.
- Ocultamiento automático de cartas que no coinciden.
- Finalización automática al encontrar los 50 pares.

## Conceptos aplicados

- Python.
- Funciones.
- Listas y listas bidimensionales.
- Ciclos `for` y `while`.
- Condicionales.
- Manejo de excepciones con `try` / `except`.
- Generación aleatoria con `random`.
- Pausas temporizadas con `time`.
- Validación de entradas del usuario.

## Estructura

- `crear_tablero()`: crea y mezcla las 100 cartas.
- `mostrar_tablero()`: imprime el estado visible del tablero.
- `pedir_coordenada()`: valida que las coordenadas sean números enteros entre 0 y 9.
- `main()`: controla el flujo completo del juego.

## Ejecución

No requiere librerías externas.

```bash
python memory_game.py
```

También puede ejecutarse directamente desde Thonny u otro IDE compatible con Python 3.

## Nota

Esta versión para portafolio conserva la lógica del proyecto académico original e incluye una pequeña mejora de robustez: la segunda selección utiliza la misma validación de coordenadas que la primera para evitar errores por entradas no válidas.

## Autor

**Juan Pablo Amezcua**  
Estudiante de Ingeniería en Tecnologías Computacionales — Tecnológico de Monterrey
