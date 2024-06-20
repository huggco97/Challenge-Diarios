# Juego de Piedra, Papel o Tijeras: 
# Escribe un programa que permita al usuario jugar piedra, papel o tijeras contra la computadora.
import random

# Opciones disponibles
opciones = ["piedra", "papel", "tijeras"]

# Función para determinar el ganador
def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return "Empate"
    elif (usuario == "piedra" and computadora == "tijeras") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijeras" and computadora == "papel"):
        return "Ganaste"
    else:
        return "Perdiste"

# Obtener la jugada del usuario
jugada_usuario = input("Elige piedra, papel o tijeras: ").lower()

# Validar la jugada del usuario
if jugada_usuario not in opciones:
    print("Elección inválida. Por favor elige piedra, papel o tijeras.")
else:
    # Generar la jugada de la computadora
    jugada_computadora = random.choice(opciones)

    # Mostrar las elecciones
    print(f"Tú elegiste: {jugada_usuario}")
    print(f"La computadora eligió: {jugada_computadora}")

    # Determinar el ganador
    resultado = determinar_ganador(jugada_usuario, jugada_computadora)
    print(f"Resultado: {resultado}")

