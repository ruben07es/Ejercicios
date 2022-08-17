"""
Escribí un programa que solicite al usuario ingresar un número con decimales y almacenalo en una variable. 
A continuación, el programa debe solicitar al usuario que ingrese un número entero y guardarlo en otra variable. 
En una tercera variable se deberá guardar el resultado de la suma de los dos números ingresados por el usuario. 
Por último, se debe mostrar en pantalla el texto “El resultado de la suma es [suma]”, 
donde “[suma]” se reemplazará por el resultado de la operación.
"""

print ("\n #################### EJERCICIO 2 #################### \n")

decimal = float(input("Introduce un número decimal: "))
entero = int(input("Introduce un número entero: "))

suma = decimal + entero

print (f"El resultado de la suma es: {suma}")