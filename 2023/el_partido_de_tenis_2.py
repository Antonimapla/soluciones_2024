

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
puntos = {}

jugador_1 = 0
jugador_2 = 0 
dato = 0
ganador = ""
dato = 1    
p1 = "p1"
p2 = "p2"
marca1 = 0
marca2 = 0
jugada = 0
            

def puntuacion(jugador):
    global jugador_1, jugador_2
    if jugador == p1:
        jugador_1 += 1
        marcador1(jugador_1, jugador_2)
    else:
        jugador_2 +=  1
        marcador2(jugador_2, jugador_1)



def diccio(jugada, ganador):
    global p1, p2
    puntos[jugada] = ganador 
    if ganador == p1:
        puntuacion(p1)
    else:
        puntuacion(p2)


        
def entrada_datos(jugada):
    global p1, p2
    jugada += 1
    ganador = input(f"Introduzca jugador ganador (p1 o p2) de la jugada {jugada}: ")
    diccio(jugada, ganador)
    return jugada 

def marcador1(jugador_1, jugador_2):
    global marca1
    puntos_P1 = jugador_1
    if puntos_P1 == 0:
        marca1 = "love"
    elif puntos_P1 == 1:
        marca1 = "15"
    elif puntos_P1 == 2:
        marca1 = "30"
    elif puntos_P1 == 3:
        marca1 = "40"
    elif puntos_P1 == 4:
        marca1 = "deuce"
    elif puntos_P1 == 5:
        marca1 = "ventaja"
    elif puntos_P1 == 6:
        marca1 = "winner"

           
    imprimir_puntuacion(marca1, marca2)
    if marca1 == "winner":
        exit()

def marcador2(jugador_2, jugador_1):
    global marca2
    puntos_P2 = jugador_2
    if puntos_P2 == 0:
        marca2 = "love"
    elif puntos_P2 == 1:
        marca2 = "15"
    elif puntos_P2 == 2:
        marca2= "30"
    elif puntos_P2 == 3:
        marca2 = "40"
    elif puntos_P2 == 4:
        marca2 = "deuce"
    elif puntos_P2 == 5:
        marca2 = "ventaja"
    elif puntos_P2 == 6:
        marca2 = "winner"
        
    imprimir_puntuacion(marca1, marca2)
    
    if marca2 == "winner":
        exit()

def imprimir_puntuacion(marca1, marca2):
    print('\n')
    print(f"JUGADA {jugada + 1}   Jugador 1 : {marca1}    Jugador 2 : {marca2}")    


x = 16
      
while x > 0:
    jugada = entrada_datos(jugada)
    x -= 1
     
        #print("Fin del juego")

print(puntos)
    
    
    
    

    
