"""
Escribí un programa que, dada una cadena de texto por el usuario, 
imprima True si la cantidad de caracteres en la cadena es un número impar, o False si no lo es.
"""

print ("\n #################### EJERCICIO 14 #################### \n")

cadena = input("Introduce la frase a comprobar: ")

numero = len(cadena)%2
if numero == 0:
    print (False)
else:
    print (True)