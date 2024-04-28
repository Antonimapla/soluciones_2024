"""
Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
"""





import random

Player1 = 0         #puntuacion jugador 1
Player2 = 0         #puntuacion jugador 2
Tie = 0             #empate
mano1 = ""          #contenido de la mano 1
mano2 = ""          #contenido de la mano 2
joc = 1             #interruptor bucle while
jugada = 1          #numero de jugadas
i = 0
lista_mano1 = []
lista_mano2 = []
mano_mano = {}
mono_mono = []
resultado = ""

opciones =['piedra', 'papel', 'tijera', 'lagarto', 'spock']     #opciones de juego

class Partida:
    
    def __init__(self):
        self.mano1 = mano1
        self.mano2 = mano2
        self.Player1 = Player1
        self.Player2 = Player2
        self.Tie = Tie
        self.jugada = jugada
        self = self
        self.opciones = opciones

    
    def eleccion_jugada(self):              #elige la opcion en la mano
        global jugada
        print(f"\nJUGADA = {jugada}")       #imrime el numero de la jugada  
        mano1 = input("JUGADOR 1 elija opcion: 1-piedra 2-papel 3-tijera 4-lagarto 5-spock = ")
        if mano1 == '1':
            mano1 = 'piedra'
        elif mano1 == '2':
            mano1 = 'papel'
        elif mano1 == '3':
            mano1 = 'tijera'
        elif mano1 == '4':
            mano1 = 'lagarto'
        elif mano1 == '5':
            mano1 = 'spock'    
        print(f"\nJUGADA = {jugada}")       #imrime el numero de la jugada
        mano2 = input("JUGADOR 2 elija opcion: 1-piedra 2-papel 3-tijera 4-lagarto 5-spock = ") 
        if mano2 == '1':
            mano2 = 'piedra'
        elif mano2 == '2':
            mano2 = 'papel'
        elif mano2 == '3':
            mano2 = 'tijera'
        elif mano2 == '4':
            mano2 = 'lagarto'
        elif mano2 == '5':
            mano2 = 'spock' 
        jugada += 1                         #aumentamos el contador de las jugadas
        ganador_jugada(mano1, mano2)        #llamamos a ganador_jugada()
    
def ganador_jugada(mano1, mano2):
        global Tie          #variables globales
        global Player1
        global Player2
        puntos = Player1    #cojemos los puntos de Player1 para hacer la comparacion y ver quien gana la jugada

        if mano1 == mano2:
            Tie +=1                                             #empate
        elif mano1 == 'piedra':
            if mano2 == 'lagarto' or mano2 == 'tijeras':
                Player1 += 1
            elif mano2 == 'spock' or mano2 == 'papel':
                Player2 += 1
        elif mano1 == 'papel':
            if mano2 == 'piedra' or mano2 == 'spock':
                Player1 += 1
            elif mano2 == 'lagarto' or mano2 == 'tijera':
                Player2 += 1   
        elif mano1 == 'tijera':
            if mano2 == 'lagarto' or mano2 == 'papel':
                Player1 += 1
            elif mano2 == 'spock' or mano2 == 'piedral':
                Player2 += 1   
        elif mano1 == 'lagarto':
            if mano2 == 'spock' or mano2 == 'papel':
                Player1 += 1
            elif mano2 == 'piedra' or mano2 == 'tijera':
                Player2 += 1  
        elif mano1 == 'spock':
            if mano2 == 'tijera' or mano2 == 'piedra':
                Player1 += 1
            elif mano2 == 'lagarto' or mano2 == 'papel':
                Player2 += 1
        if Player1 == puntos:                                   #comprobamos si el ganador es Player1, si ha aumentado 1 punto
            print(f"\nGanador de esta partida: Jugador 2")      #si no es asi el ganador es Player2
        else:
            print(f"\nGanador de esta partida: Jugador 1")      #si noes Player1, el ganador es Player2
        guarda_las_jugadas(mano1, mano2)                        #llamamos a guarda_las_jugadas()
        
def guarda_las_jugadas(mano1, mano2):
    mono_mono.append(mano1)
    mono_mono.append(mano2)
    #print(mano_mano)                    #imprimimos el diccionario
    print(f"Juegos ganados por jugador 1 = {Player1}")      #imprimimos juegos ganados por jugador 1
    print(f"Juegos ganados por jugador 2 = {Player2}")      #imprimimos juegos ganados por jugador 2
    print(f"Juegos empatados = {Tie}")                      #imprimimos empates
    
    if Player1 == Player2:          #Comprobamos si estan empatados
        resultado = 'Empate'    
    elif Player1 > Player2:         #Comprobamos si gana el jugador 1
        resultado = 'Jugador 1'
    else:
        resultado = 'Jugador 2'     #si no gana el 1 gana el 2

    
    #for i in range(0, 6):
        #if mono_mono[i]:
            #print(f"Por orden de xxxx {mono_mono[i]}, el otro {mono_mono[-1]} ")



jugon = Partida()               #creamos alias de la clase Partida
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
while joc <= 6:                 #bucle principal
    jugon.eleccion_jugada()       
    joc += 1

print(mono_mono)    


    
   