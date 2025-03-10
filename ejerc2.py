# Realizar el siguiente juego: Piedra, papel o tijeras Este es un juego muy antiguo en el que  intervienen dos personas. Cada jugador hace su elección entre las tres alternativas existentes  (piedra, papel o tijeras) y el ganador se determina atendiendo a las siguientes reglas: 

# • La piedra gana a las tijeras (puede golpearlas hasta romperlas).  
# • Las tijeras ganan al papel (pueden cortarlo).  
# • El papel gana a la piedra (puede envolverla).  
# • Si las dos elecciones son la misma se produce un empate.

import random

def determinar_ganador(jugador, comput):
    if (jugador == "piedra" and comput == "tijeras") or (jugador == "tijeras" and comput == "papel") or (jugador == "papel" and comput == "piedra"):
        return "Ganaste"
    elif jugador == comput:
        return "Empate"
    else:
        return "Perdiste"

def jugar():
    opciones = {1: "piedra", 2: "papel", 3: "tijeras"}
    
    while True:
        print("\n========== Piedra, Papel o Tijeras ==========")
        print("\n1. Piedra 🪨 \n2. Papel 🧻 \n3. Tijeras ✂️")
        
        jugOpc = int(input("\nElige una de las Opciones (1, 2 o 3): "))
        
        if jugOpc not in opciones:
            print("Opcion Invalida, Intenta Otra Vez")
            continue

        jugador = opciones[int(jugOpc)]
        print(f"\nElegiste: {jugador.upper()}")

        comput = random.choice(list(opciones.values()))
        print(f"La Computadora Eligio: {comput.upper()}")

        resultado = determinar_ganador(jugador, comput)
        print(f"\nResultado: {resultado.upper()}")
        
        jugarOtraVez = input("\n¿Quieres Jugar Otra Vez? (Si/No): ").lower()
        if jugarOtraVez != "si":
            break

jugar()