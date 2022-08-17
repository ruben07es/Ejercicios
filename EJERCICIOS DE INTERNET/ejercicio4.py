"""
Escribí un programa que solicite al usuario ingresar la cantidad de kilómetros recorridos por una motocicleta 
y la cantidad de litros de combustible que consumió durante ese recorrido. 
Mostrar el consumo de combustible por kilómetro.
"""

print ("\n #################### EJERCICIO 4 #################### \n")

kilometros = float(input("Introduce el número de kms recorridos: "))
consumo = float(input("Introduce los litros de carburante consumidos: "))

print (f"Durante el trayecto consumió: ", kilometros/consumo, " litros de carburante")