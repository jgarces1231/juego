import random

def obtener_palabra_secreta():
    palabras = ["python", "programacion", "computadora", "desarrollo", "juego", "codigo"]
    return random.choice(palabras)

def jugar_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = ['_'] * len(palabra_secreta)
    intentos_maximos = 6
    intentos_realizados = 0

    print("¡Bienvenido al Juego de Ahorcado!")
    print("Intenta adivinar la palabra secreta.")

    while True:
        print(" ".join(letras_adivinadas))

        if '_' not in letras_adivinadas:
            print("¡Felicidades! Has adivinado la palabra secreta.")
            break

        if intentos_realizados == intentos_maximos:
            print("Lo siento, has agotado tus intentos. La palabra secreta era:", palabra_secreta)
            break

        letra = input("Ingresa una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa una única letra válida.")
            continue

        if letra in palabra_secreta:
            print("¡Letra correcta!")
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] == letra:
                    letras_adivinadas[i] = letra
        else:
            print("Letra incorrecta. Te quedan", intentos_maximos - intentos_realizados - 1, "intentos.")
            intentos_realizados += 1

# Llamada a la función principal para iniciar el juego
jugar_ahorcado()
