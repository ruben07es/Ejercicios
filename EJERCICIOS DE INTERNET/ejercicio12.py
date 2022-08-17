"""
Escribí un programa para solicitar al usuario el ingreso de un número entero 
y que luego imprima un valor de verdad dependiendo de si el número es par o no. 
Recordar que un número es par si el resto, al dividirlo por 2, es 0.
"""

print ("\n #################### EJERCICIO 12 #################### \n")

numero = int(input("Ingresa un número entero: "))
resto = numero %2
if resto == 0:
    print (f"El número es par")
else:
    print (f"El número es impar")
