
lista_mano1 = []
lista_mano2 = []
mano_mano = {}
Player1 = 0         #puntuacion jugador 1
Player2 = 0

opcion: [1-piedra 2-papel 3-tijera 4-lagarto 5-spock]

def guarda_las_jugadas(mano1, mano2):

    mano_mano[mano1] = mano2            #llenamos un diccionario con clave (jugador1) y valor (jugador 2)
    print(mano_mano)                    #imprimimos el diccionario
    print(f"Juegos ganados por jugador 1 = {Player1}")      #imprimimos juegos ganados por jugador 1
    print(f"Juegos ganados por jugador 2 = {Player2}")      #imprimimos juegos ganados por jugador 2
    print(f"Juegos empatados = {Tie}")                      #imprimimos empates