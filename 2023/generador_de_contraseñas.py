"""
Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
""" 
import random
from random import sample
import numpy as np

letras_minus = "abcdefghijklmnopqrstuvwxyz"
letras_mayus = letras_minus.upper()
numeros = "0123456789"
simbolos = "{}[]*;/,_-"
opciones = {}
longitud = 0 
contraseña = []
tamano = 0 
listado_todo = str(longitud) + letras_minus + letras_mayus + numeros + simbolos



def introducir_datos():
    print('\n')
    longitud = input("Que longitud quiere en la contraseña de 8 a 16 caracteres?: ")
    opciones['longitud'] = longitud  
    opciones['letras_minus'] = 's'
    mayusculas = input("Con letras mayusculas S / N ?: ")
    opciones['letras_mayus'] = mayusculas
    numeros = input("Con numeros S / N ?: ")
    opciones['numeros'] = numeros
    simbolos = input("Con simbolos S / N ?: ")
    opciones['simbolos'] = simbolos
    largo = int(longitud)
    
    preparar_contraseñas(listado_todo, opciones, largo)
    
def preparar_contraseñas(listado_todo, opciones, largo):
    lista = []
    listado = [letras_minus]
    #if opciones['letras_mayus'] == 's':
        #listado.append(letras_mayus)
    for respuesta in opciones.values():
        lista.append(respuesta)
    if lista[2] == 's':
        listado.append(letras_mayus)
    if lista[3] == 's':
        listado.append(numeros)
    if lista[4] == 's':
        listado.append(simbolos)
    
    generar_contraseña(listado, largo)



def generar_contraseña(listado, largo):
    total = "".join(listado)
    tamano = int(longitud)
    print(total)
    password = [total[np.random.randint(low=0, high=len(total))] for i in range(largo)]
    password1 = "".join(password)
    print("\n")
    print(password1)
    print("\n")




           
    





introducir_datos()