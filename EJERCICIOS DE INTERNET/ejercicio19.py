"""
Escribí un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “Es vocal”. 
Verificar si el usuario ingresó un string de más de un carácter y, en ese caso, informarle que no se puede procesar el dato.
"""

letra = input("introduce una letra: ")
letra_min = letra.lower ()
vocales = ["a", "e", "i", "o", "u"]

if len(letra) == 1:
    if letra_min in vocales:
        print (f"{letra}: Es una vocal")
    else:
        print (f"{letra}: Es una consonante")
else:
    print ("No se puede procesar el dato")