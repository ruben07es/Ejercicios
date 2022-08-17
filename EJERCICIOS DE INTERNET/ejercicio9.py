"""
Escribí un programa que solicite al usuario el ingreso de un texto y almacene ese texto en una variable. 
A continuación, mostrar en pantalla la primera letra del texto ingresado. 
Luego, solicitar al usuario que ingrese un número positivo menor a la cantidad de caracteres 
que tiene el texto que ingresó (por ejemplo, si escribió la palabra “HOLA”, tendrá que ser un número entre 0 y 4) 
y almacenar este número en una variable llamada indice.
Mostrar en pantalla el carácter del texto ubicado en la posición dada por indice.
"""

print ("\n #################### EJERCICIO 9 #################### \n")

texto = input ("Introduce una frase: ")
longitud_texto = len (texto)
cont = 0
for i in texto:
    if cont<1:
        print (i)
    cont += 1
indice = int(input(f"Introduce un número positivo inferior a {longitud_texto}: "))

print (texto [indice])