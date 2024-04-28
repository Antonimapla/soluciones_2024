"""
Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
"""

numero = input("Intruduzca un numero: ")
#**********secuencia de fiboracci ****************************************
i = 0

def fiboracci():        #calculamos la secuencia de fiboracci
    x = 0               #variable para contener el segundo numero anterior al actual
    y = 1               #variable para contener el primer numero anterior al actual
    listado = []        #lista para contener la secuencia
    fibor = 0           #entero para contener el numero de fiboracci
   
    for i in range(0, 50):      #calculamos los 50 primeros numeros de la secuencia 
        if i == 0:
            listado.append(1)   #primer numero de la secuencia
        elif i == 1:
            listado.append(1)   #segundo numero de la secuencia
        else: 
            x = listado[i-2]    #suma de los dos anteriores
            y = listado[i-1]
            fibor = x + y
            listado.append(fibor)   #añadimos numero al listado de la secuencia
    #for i in listado:
    
    if int(numero) in listado:      #comprobamos si el numero solicitado esta en la secuencia e imprimimos la respuesta.
        print(f"El numero {numero} esta en la secuencia de fiboracci.")
    else:
        print(f"El numero {numero} no esta en la secuencia de fiboracci.")

#************** es par ********************************************************
def es_par():
    if int(numero) % 2 == 0:                    #comprobamos si el numero es par, haciendo el modulo resto
        print(f"El numero {numero} es par.")
    else:
        print(f"El numero {numero} es impar.")
        
#****************** es primo ***************************************************
def es_primo():
    
    lista = list(numero)         
    print(lista)                       #convertimos numero en una lista
    total = 0
    if lista[-1] == 0 or lista[-1] == 5:                #comprobamos si es divisible por 5
        print(f"El numero {numero} no es primo1.")
        
    elif int(numero) % 2 == 0:                          #comprobamos si es par
        print(f"El numero {numero} no es primo2.")
        
    elif int(numero) < 10:                              #si el numero es menor de 10 lo comparamos directamente
        primos = [2, 3, 5, 7]
        if int(numero) in primos:
            print(f"El numero {numero} es primo3.")
    else:
        numeros = numero.split()                        #convertimos el numero en una lista de caracteres separados
        for num in range(len(numeros) + 1):             #bucle  para poder sumar los digitos que componen el numero
            total += int(lista[num])                    #total de la suma de los digitos
        if total % 3 == 0:                              #comprobamos si es divisible por 3
            print(f"El numero {numero} no es primo4.")
        else:
            print(f"El numero {numero} es primo5.")
        
        
fiboracci()
es_par()
es_primo()
