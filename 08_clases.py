### 08-clases
"""Creacion de una clase que representa un gato y alguna de sus habilidades"""
class Gat:

    def __init__(self, nombre, edad):
        #inicializacion de atributos
        self.nombre = nombre
        self.edad = edad

    def sentado(self):
        #el gato se sienta
        print(f"{self.nombre} esta sentado.")
    
    def corre(self):
        #el gato empieza a correr 
        print(f"{self.nombre} esta corriendo")

    def imprimir(self):
        print(f"Mi gato se llama {self.nombre}")
        print(f"Mi gato tiene {self.edad} años.")

mi_gato = Gat("Misi", 2)
mi_gato.imprimir()
mi_gato.sentado()
mi_gato.corre()