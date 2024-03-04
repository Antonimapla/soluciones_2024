

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

puntos = 0
puntos_P1 = 0
puntos_P2 = 0
juego = 0
pset = 0
#ganador = 
puntos1 = ["love", "15", "30", "40", "deuce", "ventaja", "winner"]
puntos2 = ["love", "15", "30", "40", "deuce", "ventaja", "winner"]
p1 = 0
p2 = 0
bola = True
marca1 = ""
marca2 = ""


while bola == True:

    #def ganador_pset():
    ganador = input("Introduzca jugador ganador p1 - p2: ")
        #return ganador
    
    p1p2 = ganador

    def reset_contadores():
        puntos_P1 = 0
        puntos_P2 = 0

    
    
    def progreso_juego(p1p2):
        if p1p2 == p1:
            puntos_P1 += 1
            marcador(puntos_P1)

        elif p1p2 == p2:
            puntos_P2 += 1
            marcador(puntos_P2)

    progreso_juego(p1p2)

    def marcador(p1p2):
        puntos1 = ["love", "15", "30", "40", "deuce", "ventaja", "winner"]
        puntos2 = ["love", "15", "30", "40", "deuce", "ventaja", "winner"]

        if puntos_P1 == 1:
            marca1 = "love"
        elif puntos_P1 == 2:
            marca1 = "15"
        elif puntos_P1 == 3:
            marca1 = "30"
        elif puntos_P1 == 4:
            marca1 = "40"
        elif puntos_P1 == 5:
            marca1 = "deuce"
        elif puntos_P1 == 6:
            marca1 = "ventaja"
        elif puntos_P1 == 7:
            marca1 = "winner"
        else: 
            if puntos_P2 == 1:
                marca2 = "love"
            elif puntos_P2 == 2:
                marca2 = "15"
            elif puntos_P2 == 3:
                marca2= "30"
            elif puntos_P2 == 4:
                marca2 = "40"
            elif puntos_P2 == 5:
                marca2 = "deuce"
            elif puntos_P2 == 6:
                marca2 = "ventaja"
            elif puntos_P2 == 7:
                marca2 = "winner"

        print(f"Resultado provisional del partido jugador1 {marca1}")
        print(f"Resultado provisional del partido jugador2 {marca2}")

    
    if marca1 or marca2== "winner":
       reset_contadores()
       bola = False        





        
    
    
