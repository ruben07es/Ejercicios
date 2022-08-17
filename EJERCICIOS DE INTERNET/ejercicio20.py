"""
Escribí un programa para solicitar al usuario tres números y mostrar en pantalla al menor de los tres.
"""

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
numero3 = int(input("Introduce el tercer número: "))

if numero1 < numero2 and numero1 < numero3:
    print (f"El menor es: {numero1}")
elif numero2 < numero1 and numero2 < numero3:
    print (f"El menor es: {numero2}")
elif numero3 < numero1 and numero3 < numero2:
    print (f"El menor es: {numero3}")