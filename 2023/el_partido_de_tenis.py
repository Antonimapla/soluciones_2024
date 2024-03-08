import time

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
class Tenis:
    #simulacion de una partida de tenis
    def __init__(self) -> None:
        self.puntos = ["love", "15", "30", "40", "deuce", "ventaja", "winner"]
        self.jugada = 0
        self.puntos_P1 = 0
        self.puntos_P2 = 0
        self.ganador = ""
        self.jugador_1 = 0
        self.jugador_2 = 0 
        self.tennis = Tenis
        
    def partido(self):
        self.jugada += 1
        self.ganador = input(f"Introduce ganador de la {self.jugada}: ")
        puntuacion(self, ganador)



    def puntuacion(self, ganador):
        if self.ganador == self.jugador_1:
            self.puntos_P1 += 1
            marcador_jugador_1(self, self.puntos_P1)
        else:
            self.puntos_P2 += 1
            marcador_jugador_2(self, self.puntos_P2)


    
    def marcador_jugador_1(self, puntos):
        for i in puntos:
            if puntos[i] == self.puntos_P1:
                print(f"Puntuacion jugador 1: {puntos[i]}")
    

    def marcador_jugador_2(self, puntos):
        for i in puntos:
            if puntos[i] == self.puntos_P2:
                print(f"Puntuacion jugador 2: {puntos[i]}")
    
    tennis.partido(jugada)

tennis = Tenis
        





    
    
"""
for i in range(1, 5):
    
    def ganador_pset():
        ganador = input("Introduzca jugador ganador p1 - p2: ")
        print(ganador)
        p1p2 = ganador
        progreso_juego(p1p2)

    def progreso_juego(p1p2):
        if p1p2 == p1:
            puntos_P1 += 1
            print(puntos_P1)
            marcador(puntos_P1)

        elif p1p2 == p2:
            puntos_P2 += 1
            time.sleep(5)
            marcador(puntos_P2)

    def marcador(p1p2):
        print(p1p2)
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
            
    print(f"Resultado provisional del partido jugador1:{marca1}")
    print(f"Resultado provisional del partido jugador2:{marca2}")
    
    if marca1 or marca2== "winner":
        bola += 1
        if marca1 == "winner":
            print("El ganador es: Jugador 1")
        else:
            print("El ganador es: Jugador 2")

                       
ganador_pset()
  
progreso_juego(p1p2)

def reset_contadores():
        puntos_P1 = 0
        puntos_P2 = 0

exit()    
        
    
    
"""