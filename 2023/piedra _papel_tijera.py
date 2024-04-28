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

opciones =['piedra', 'papel', 'tijera', 'lagarto', 'spock']     #opciones de juego

while joc:
        mano1 = ""
        mano2 = "" 

    def eleccion_jugada(mano1, mano2):
        global jugada
        print(f"\nJUGADA = {jugada}")   #elige la opcion en la mano
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
        #print(f"LINEA 43 {mano1}")
        print(f"\nJUGADA = {jugada}")   #elige la opcion en la mano
        mano2 = input("JUGADOR 2 elija opcion: 1-piedra 2-papel 3-tijera 4-lagarto 5-spock = ") 
        #print(f"LINEA 46 {mano1}")
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
        #print(f"LINEA 56 {mano2}") 
        jugada += 1   
        ganador_jugada(mano1, mano2)
    


    def ganador_jugada(mano1, mano2):
        #print(f"LINEA 65 {mano1}")
        global Tie
        global Player1
        global Player2
        if mano1 == mano2:
            #print(f"linea 70 {mano1}")
            Tie +=1
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
        #print(f"HOla 97, {mano1}")
        guarda_las_jugadas(mano1, mano2)
    

    def guarda_las_jugadas(mano1, mano2):
        #print(f"linea 105 {mano1}")
    
        list    a_mano1.append(mano1)
        lista_mano2.append(mano2)
        #print(lista_mano1)


        """
        for i in lista_mano1:
            print(lista_mano1)
            print(lista_mano2)
        """

eleccion_jugada(mano1, mano2)
    #print(f"LINEA 112 {mano1}")
    #guarda_las_jugadas(mano1, mano2)
   