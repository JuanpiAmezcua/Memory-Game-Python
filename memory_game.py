import random
import time


def crear_tablero():
    emojis = [
        '😀', '😎', '🥳', '🤖', '🐶', '🐱', '🐭', '🐹', '🐰', '🦊',
        '🐻', '🐼', '🐨', '🐯', '🦁', '🐮', '🐷', '🐸', '🐵', '🐔',
        '🐧', '🐦', '🐤', '🐣', '🦆', '🦉', '🦇', '🐺', '🦄', '🐝',
        '🐛', '🦋', '🐌', '🐞', '🐢', '🐍', '🦖', '🐙', '🦀', '🐡',
        '🐠', '🐳', '🦈', '🐊', '🦓', '🦒', '🐘', '🐫', '🦘', '🐿️'
    ]

    cartas = emojis * 2
    random.shuffle(cartas)

    tablero = []
    for i in range(10):
        fila = cartas[i * 10:(i + 1) * 10]
        tablero.append(fila)

    return tablero


def mostrar_tablero(tablero_visible):
    columnas = "    " + "  ".join(str(i) for i in range(10))
    print("\n" + columnas)

    for i in range(10):
        fila = " ".join(tablero_visible[i])
        print(f"{i} {fila}")


def pedir_coordenada(texto):
    while True:
        try:
            valor = int(input(texto))

            if 0 <= valor <= 9:
                return valor

            print("Por favor ingrese un número entre 0 y 9.")

        except ValueError:
            print("Solo utilice números enteros para indicar las cartas.")


def main():
    tablero = crear_tablero()
    tablero_visible = [['⬜' for _ in range(10)] for _ in range(10)]

    aciertos = 0
    intentos = 0

    print("=== ¡Bienvenido al Memorama! ===")

    while aciertos < 50:
        mostrar_tablero(tablero_visible)

        x1 = pedir_coordenada("Ingresa fila de la primera carta (0-9): ")
        y1 = pedir_coordenada("Ingresa columna de la primera carta (0-9): ")

        if tablero_visible[x1][y1] != '⬜':
            print("Esta carta ya fue descubierta. Elige otra.")
            continue

        tablero_visible[x1][y1] = tablero[x1][y1]
        mostrar_tablero(tablero_visible)

        while True:
            x2 = pedir_coordenada("Ingresa fila de la segunda carta (0-9): ")
            y2 = pedir_coordenada("Ingresa columna de la segunda carta (0-9): ")

            if x2 == x1 and y2 == y1:
                print("Esta carta ya fue seleccionada. Intenta con otra.")
                continue

            if tablero_visible[x2][y2] != '⬜':
                print("Esta carta ya fue descubierta. Elige otra.")
                continue

            break

        tablero_visible[x2][y2] = tablero[x2][y2]
        mostrar_tablero(tablero_visible)

        intentos += 1

        if tablero[x1][y1] == tablero[x2][y2]:
            print("¡Encontraste un par!")
            aciertos += 1
        else:
            print("No coinciden. Se ocultarán en 5 segundos...")
            time.sleep(5)

            tablero_visible[x1][y1] = '⬜'
            tablero_visible[x2][y2] = '⬜'

    print(f"\n¡Felicidades! Encontraste todos los pares en {intentos} intentos.")


if __name__ == "__main__":
    main()
