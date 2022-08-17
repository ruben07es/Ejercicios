"""
Escribí un programa que solicite al usuario el ingreso de una temperatura en escala Fahrenheit 
(debe permitir decimales) y le muestre el equivalente en grados Celsius. 
La fórmula de conversión que se usa para este cálculo es: _Celsius = (5/9) * (Fahrenheit-32)_
"""

print ("\n #################### EJERCICIO 5 #################### \n")

farenheit = float (input("Introduce la temperatura en ºF: "))
celsius = (5/9) * (farenheit  - 32)

print (f"La temperatura en ºC es {celsius}")