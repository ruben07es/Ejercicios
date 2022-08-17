"""
Escribí un programa que le solicite al usuario un número entero y 
muestre todos los números correlativos entre el 1 y el número ingresado por el usuario.
"""

numero = int(input("Introduce un número: "))
i = 0

for i in range (1,numero+1):
    print (i)
    i += 1