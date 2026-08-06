import random
import sys

INTENTOS_MAXIMOS = 5
def elegir_dificultad():

    # Preguntamos al jugador que nivel quiere jugar
    # de acuerdo a la repuesta se define el nivel de dificultad.

    print("\nElige un nivel de dificultad:")
    print("1. Facil   (1-10)")
    print("2. Medio   (1-20)")
    print("3. Dificil (1-50)")

    while True:
        opcion = input("Opción (1/2/3): ").strip()

        if opcion == "1":
            return 1, 10
        elif opcion == "2":
            return 1, 20
        elif opcion == "3":
            return 1, 50
        else:
            print("Opcion invalida, intente de nuevo (1, 2 o 3).")

def pedir_numero(minimo, maximo):
    # funcion aparte para validar que lo que escriba el jugador
    # sea realmente un numero, si no le sigo pidiendo
    while True:
        entrada = input(f"Ingresa un numero entre {minimo} y {maximo}: ")

        if not entrada.isdigit():
            print("Número valido, intente otra vez.")
            continue

        numero = int(entrada)

        if numero < minimo or numero > maximo:
            print(f"Número no esta en el rango entre {minimo} y {maximo}.")
            continue

        return numero

def jugar_una_partida():
    minimo, maximo = elegir_dificultad()
    numero_secreto = random.randint(minimo, maximo)

    print(f"\nTengo un número secreto listo. ¿Puedes adivinarlo? {minimo} y {maximo}.")
    print(f"Tienes {INTENTOS_MAXIMOS} intentos para adivinarlo. Suerte!\n")

    intentos_usados = 0

    while intentos_usados < INTENTOS_MAXIMOS:
        intento = pedir_numero(minimo, maximo)
        intentos_usados += 1

        if intento == numero_secreto:
            print(f"\nLo haz logrado! El numero era {numero_secreto}.")
            print(f"Lo adivinaste en {intentos_usados} intento(s).")
            return

        if intento < numero_secreto:
            print("El numero secreto es MAYOR que ese.")
        else:
            print("El numero secreto es MENOR que ese.")

        intentos_restantes = INTENTOS_MAXIMOS - intentos_usados

        if intentos_restantes > 0:
            print(f"Te quedan {intentos_restantes} intento(s).\n")

    # si llega hasta aca es porque se le acabaron los intentos
    print(f"\nSe agotaron los intentos. El numero secreto era {numero_secreto}.")

def preguntar_si_repite():
    while True:
        respuesta = input("\nQuieres jugar otra vez? (s/n): ").lower().strip()

        if respuesta == "s":
            return True
        elif respuesta == "n":
            return False
        else:
            print("Por favor responde con 's' o 'n'.")

def main():
    print("=== ADIVINA EL NUMERO SECRETO ===")

    seguir_jugando = True

    while seguir_jugando:
        jugar_una_partida()
        seguir_jugando = preguntar_si_repite()

    print("\nGracias por jugar, hasta la proxima!")

if __name__ == "__main__":
    main()
