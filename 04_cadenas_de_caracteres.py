        ### operaciones con cadenas de caracteres ###

texto = """Luego, tenemos que la suma es igual a la suma más el valor,
así que 9, 50, 62, 65, 139, 54, por lo que este es el total acumulado. 
Esta es la cuenta.En realidad, esa es la suma en este caso, la variable 
de suma."""

# acceso a caracteres especificos
longo = len(texto)      # longitud de la cadena
print(longo)
lista = list(texto)
print(lista)
caracter = 0
for i in range(len(lista)):
    print(caracter, lista[i]) #acceso a cualquier caracter con lista[numero]
    caracter += 1

#acceso a subcadena
subcadena = lista[41:45]    #acedemos a la subcadena suma
print(subcadena)

#concatenacion
a = "Buenas"
b = "noches"
print(a + " " + b)

#repeticion
x = "hola"
y = 5
print("hola" * y)

#recorrido
c = "platano"
letra = c[0]
print(letra)

