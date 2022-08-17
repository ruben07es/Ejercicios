"""
Escribí un programa que permita al usuario ingresar una frase y luego un carácter (string de longitud 1) 
y luego muestre la frase ingresada, pero con todas las ocurrencias del carácter indicado por el usuario reemplazadas por “*”.
"""


frase = input ("Introduce una frase: ")
letra = input ("Introduce la letra a codificar: ")

print (frase.replace(letra, "*"))
