"""
.Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
"""

puntos = []
puntos_P1 = 0
puntos_P2 = 0
juego = 0
pset = 0
ganador = ""
puntos1 = ["love", "15", "30", "40", "deuce", "ventaja", "winner"]
puntos2 = ["love", "15", "30", "40", "deuce", "ventaja", "winner"]
p1 = 0
p2 = 0

def ganador_pset():
    ganador = input("Introduzca jugador ganador p1 / p2: ")
    return ganador

p1p2 = ganador_pset()

def marcador(p1p2):
    if p1p2 == p1:
        pass






    
def puntos_jugadores(p1p2):
    pass
    
