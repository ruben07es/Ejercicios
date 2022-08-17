"""
Escribí un programa que le pida al usuario ingresar dos palabras y las guarde en dos variables, 
y que luego imprima True si la primera palabra es menor que la segunda o False si no lo es.
"""

print ("\n #################### EJERCICIO 15 #################### \n")

palabra1 = input ("Introduce la primera palabra: ")
palabra2 = input ("Introduce la segunda palabra: ")

if len(palabra1) < len(palabra2):
    print (True)
else:
    print (False)