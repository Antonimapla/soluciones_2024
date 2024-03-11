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

letras_minus = "abcdefghijklmnopqrstuvwxyz"
letras_mayus = letras_minus.upper()
numeros = "0123456789"
simbolos = "{}[]*;/,_-"
opciones = {}
longitud = 8
contraseña = ""

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
    preparar_contraseñas(listado_todo, opciones)
    
    
def preparar_contraseñas(listado_todo, opciones):
    lista = []
    listado = [letras_minus]
    #if opciones['letras_mayus'] == 's':
        #listado.append(letras_mayus)
    print(opciones)
    for respuesta in opciones.values():
        lista.append(respuesta)
    if lista[2] == 's':
        listado.append(letras_mayus)
    if lista[3] == 's':
        listado.append(numeros)
    if lista[4] == 's':
        listado.append(simbolos)
    generar_contraseña(listado)

def generar_contraseña(listado):
    total = "".join(listado)
    final = sample(listado, 8)            
    print(final)





introducir_datos()