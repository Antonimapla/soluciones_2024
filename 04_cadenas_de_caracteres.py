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

#conversion a mayusculas
TEXTO = texto.upper()
print(TEXTO)

#conversion a minusculas
minus = texto.lower()
print(minus)

#reemplazo subcadena
print(texto)
new_text = texto.replace("suma", "adicion")
print(new_text)

#division de cadenas
cadena = "tenemos que la adicion es igual a la adicion más el valor"
print(cadena.split(None, 5))

#union de cadenas
empleados = ["Juan Botas", "Luis Campos", "Pedro Botero", "Jesus Gracias"]
print(empleados)
union = " - ".join(empleados)
print(union)

#interpolacion de cadenas
nombre = "Luis"
edad = 45
print(f"El señor {nombre} tiene {edad} años.")

#verificacion de cadenas
cadena_alfanum = "Estoyenelnumero768"
cadena_alpha = "Estaesunacadenaalfabetica"
cadena_num = "456789"

if cadena_alfanum.isalnum():
    print(f"La cadena {cadena_alfanum} es alphanumerica.")
else:
    print(f"La cadena {cadena_alfanum} no es alphanumerica.")

if cadena_alpha.isalpha():
    print(f"La cadena {cadena_alpha} es alfabetica.")
else:
    print(f"La cadena {cadena_alpha} no es alphanumerica.")

if cadena_num.isdigit():
    print(f"La cadena {cadena_num} es numerica.")
else:
    print(f"La cadena {cadena_num} no es numerica.")


