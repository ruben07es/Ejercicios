
"""
Escribí un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en el último año 
y almacene ese número en una variable. A continuación mostrar en pantalla un valor de verdad (True o False) 
que indique si el usuario ha visto más de 3 shows. 
"""

print ("\n #################### EJERCICIO 10 #################### \n")

def num_shows():
    shows = int(input("¿Cuantos shows has visto en el último año?: "))
    if shows > 3:
        return True
    else:
        return False

print (num_shows())